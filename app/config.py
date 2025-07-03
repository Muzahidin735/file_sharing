import os
from pydantic_settings import BaseSettings, SettingsConfigDict

SECRET_KEY = "YOUR_SECRET_KEY"
ALGORITHM = "HS256"
UPLOAD_DIRECTORY = "uploads"
os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)
   

class Settings(BaseSettings):
    MAIL_USERNAME: str 
    MAIL_PASSWORD: str
    MAIL_FROM: str 
    MAIL_PORT: int 
    MAIL_SERVER: str
    MAIL_TLS: bool
    MAIL_SSL: bool

model_config = SettingsConfigDict(
            env_file="mode"
        )

