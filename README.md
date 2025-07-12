## A REST API built with FastAPI and PostgreSQL that enables secure email registration, email verification, file uploads, and secure file download using secure link.

🚀**Features**\
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
• **FastAPI (Python web framework)**

• **PostgreSQL (Relational database)**

• **SQLAlchemy (ORM)**

• **JWT (Authentication)**

• **SMTP/Email Service (Email verification)**



📦 **Getting Started**\
 Prerequisites
 • Python 3.8+
 • PostgreSQL



📖**API Endpoints**

| Method | Endpoint                    | Description                       |
|--------|-----------------------------|-----------------------------------|
| POST   | `/signup`                   | Register new user                 |
| POST   | `/login`                    | User login, returns JWT           |
| POST   | `/verify-email`             | Verify email with token           |
| POST   | `/upload`                   | Upload a file                     |
| GET    | `/files`                    | List user's uploaded files        |
| GET    | `/download/{file_id}`       | Get secure download link          |
| GET    | `/secure-download/{token}`  | Download file via secure link     |



🔑 **Usage Guide**\
**Sign Up**
• Register with your email and password via /signup.

**Email Verification**
• Click the verification link sent to your email to activate your account.

**Login**
• Obtain a JWT token via /login for authenticated requests.

**Upload Files**
• Use /upload with your JWT token to upload files.

**List Files**
• Retrieve your uploaded files from /files.

**Download Files**
• Request a download link via /download/{file_id} and use the provided secure link to download.




🛡️ **Security**\
• Passwords are hashed before storage.

• JWT tokens secure all authenticated endpoints.

• Download links are time-limited and single-use.

• Input validation and error handling implemented.


