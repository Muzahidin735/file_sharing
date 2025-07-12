## A REST API built with FastAPI and PostgreSQL that enables secure email registration, email verification, file uploads, and secure file download using secure link.

🚀**Features**/
• **User Registration & Login.**\
  Secure user authentication with hashed passwords and JWT tokens.\
• **Email Verification.**\
  Sends a verification email upon signup to activate user accounts.\
• **File Upload & Listing.**\
  Authenticated users can upload files and view their uploads.\
• **Secure File Download.**\
  Generates time-limited, secure download links for user files.\
• **PostgreSQL Integration.**\
  Stores user and file metadata efficiently.

🛠️**Tech Stack** \
• **FastAPI (Python web framework)**\
• **PostgreSQL (Relational database)**\
• **SQLAlchemy (ORM)**\
• **JWT (Authentication)**\
• **SMTP/Email Service (Email verification)**

| Method | Endpoint                    | Description                       |
|--------|-----------------------------|-----------------------------------|
| POST   | `/signup`                   | Register new user                 |
| POST   | `/login`                    | User login, returns JWT           |
| POST   | `/verify-email`             | Verify email with token           |
| POST   | `/upload`                   | Upload a file                     |
| GET    | `/files`                    | List user's uploaded files        |
| GET    | `/download/{file_id}`       | Get secure download link          |
| GET    | `/secure-download/{token}`  | Download file via secure link     |


📖**API Endpoints**\
**Methods        Endpoint                    Description**\
POST            //signup                      Register new user\
POST            //login                       User login, returns JWT\
POST            //verify-email                Verify email with token\
POST            //upload                      Upload a file\
GET             //files                       List user's uploaded files\
GET             //download/{file_id}          Get secure download link\
GET             //secure-download/{token}     Download file via secure link\
