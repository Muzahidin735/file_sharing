
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from .config import Settings

settings = Settings()

conf = ConnectionConfig(
    MAIL_USERNAME=settings.MAIL_USERNAME,
    MAIL_PASSWORD=settings.MAIL_PASSWORD,
    MAIL_FROM=settings.MAIL_FROM,
    MAIL_PORT=settings.MAIL_PORT,
    MAIL_SERVER=settings.MAIL_SERVER,
    MAIL_TLS=settings.MAIL_TLS,
    MAIL_SSL=settings.MAIL_SSL,
    USE_CREDENTIALS=True
)

async def send_verification_email(email, verification_url):
    message = MessageSchema(
        subject="Verify your email",
        recipients=[email],
        body=f"Click to verify: {verification_url}",
        subtype="html"
    )
    fm = FastMail(conf)
    await fm.send_message(message)
