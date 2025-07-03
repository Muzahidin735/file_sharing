from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from .database import Base, engine, get_db
from .database import get_db
from sqlalchemy.orm import Session
from .mycrud import get_users, get_user_by_email
#from .models import User
from .config import SECRET_KEY, ALGORITHM

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

def verify_pass(password, original_pass):
    return (password == original_pass)

def authenticate_user(email: str, password: str, db: Session = Depends(get_db)):
    get_users(db)
    user = get_user_by_email(db, email)
    #if not user or not verify_password(password, user["hashed_password"]):
    if not user or not verify_pass(password, user["password"]):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return user

def create_verification_token(email):
    expire = datetime.now(timezone.utc) + timedelta(hours=1)
    to_encode = {"sub": email, "exp": expire}
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def create_access_token(data: dict):
    to_encode = data.copy()
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def create_download_token(filename: str, expires_delta: timedelta = timedelta(minutes=10)):
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode = {"filename": filename, "exp": expire}
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token

def generate_secure_download_url(filename: str):
    token = create_download_token(filename)
    # This URL can be sent to the client
    return f"http://example.com/secure-download/{token}"

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user_by_email(db, email)
    if user is None:
        raise credentials_exception
    return user


def role_required(allowed_roles, email : str, db: Session = Depends(get_db)):
        user = get_user_by_email(db, email)
        if user["role"] not in allowed_roles:
            raise HTTPException(status_code=403, detail="Insufficient permissions")
        return user
