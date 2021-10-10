import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # config for gmail
    # MAIL_SERVER = "smtp.gmail.com"
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get("MAIL_USER")
    # MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    # MAIL_SENDER = os.environ.get("MAIL_SENDER")
