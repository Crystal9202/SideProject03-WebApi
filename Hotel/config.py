import os
from datetime import timedelta

class Config:
    #SQLALCHEMY_DATABASE_URI= "sqlite:///data.db"
    SQLALCHEMY_DATABASE_URI= f"mysql+pymysql://root:{os.getenv('PASSWORD')}@localhost:3306/hotel"
    SQLALCHEMY_TRACK_MODIFICATIONS= False
    JWT_EXPIRATION_DELTA :timedelta(seconds = 300)
    JWT_AUTH_URL_RULE = "/auth/login"
    SECRET_KEY="flask123"
    JWT_AUTH_HEADER_PREFIX = "FLASK"