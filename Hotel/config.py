import os

class Config:
    #SQLALCHEMY_DATABASE_URI= "sqlite:///data.db"
    SQLALCHEMY_DATABASE_URI= f"mysql+pymysql://root:{os.getenv('PASSWORD')}@localhost:3306/hotel"
    SQLALCHEMY_TRACK_MODIFICATIONS= False
    SECRET_KEY="flask123"