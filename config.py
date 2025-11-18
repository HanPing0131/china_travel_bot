import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = "dev-secret-key-change-this"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "travel_bot.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Email configuration (will be used later)
    MAIL_SERVER = "smtp.example.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "your_email@example.com"
    MAIL_PASSWORD = "your_password"
