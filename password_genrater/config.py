import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "super-secret-key-change-this"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///password_manager.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
