from fastapi import Form

class CustomSignUpForm:
    def __init__(
        self,
        username: str = Form(...),
        password: str = Form(...),
        email: str = Form(...)
    ):
        self.username = username
        self.password = password
        self.email = email
