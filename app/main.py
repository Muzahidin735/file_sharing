from fastapi import FastAPI, Depends, UploadFile, File, HTTPException, Query
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import FileResponse
from jose import JWTError, jwt
from .dependencies.form import CustomSignUpForm
#from .send_mail import send_verification_email
from .config import SECRET_KEY, ALGORITHM
from .auth import authenticate_user, create_access_token, role_required, generate_secure_download_url, create_verification_token
from .storage import save_file, list_files, file_path
from sqlalchemy.orm import Session
from .database import Base, engine, get_db
#from models import User
from .mycrud import get_user_by_email, create_user, get_users
from .myschema import UserCreate, UserOut

app = FastAPI()


Base.metadata.create_all(bind=engine)

@app.post("/users/", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@app.get("/users/", response_model=list[UserOut])
def read_users(db: Session = Depends(get_db)):
    return get_users(db)

@app.get("/users/by-email/", response_model=UserOut)
def get_user(email: str, db: Session = Depends(get_db)):
    user = get_user_by_email(db, email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    access_token = create_access_token({"sub": user["email"]})
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/sign-up")
async def sign_up(form_data: CustomSignUpForm = Depends()):
    username = form_data.username
    userpass = form_data.password
    useremail = form_data.email
    token = create_verification_token(useremail)
    verification_url = f"http://example.com/verify-email?token={token}"
    #await send_verification_email(useremail, verification_url)

@app.post("/upload", dependencies=[role_required(["admin"])])
async def upload_file(file: UploadFile = File(...)):
    filename = save_file(file)
    return {"filename": filename}

@app.get("/download/{filename}", dependencies=[role_required(["admin", "user"])])
async def download_file(filename: str):
    url = generate_secure_download_url(filename)
    return {"download_url": url}

@app.get("/files", dependencies=[role_required(["admin", "user"])])
async def files():
    return {"files": list_files()}

@app.get("/secure-download/{token}")
async def secure_download(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        filename = payload.get("filename")
        if not filename:
            raise HTTPException(status_code=400, detail="Invalid token")
        return FileResponse(file_path(filename), filename=filename)
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Link expired")
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    
@app.get("/verify-email")
async def verify_email(token: str = Query(...)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if not email:
            raise HTTPException(status_code=400, detail="Invalid token")
        
        user = get_user_by_email(email)
        if user:
            user["is_verified"] = True
        return {"message": "Email successfully verified!"}
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=400, detail="Verification link expired")
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid verification link")