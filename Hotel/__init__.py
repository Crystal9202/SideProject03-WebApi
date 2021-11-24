import os
from flask import Flask
from flask_restful import Api, Resource ,reqparse ,abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



db=SQLAlchemy()
from Hotel.model.user  import UserModel 
from Hotel.resource.user import UserList , User 

def create_app():   #工廠函數
    app=Flask('Hotel')
    # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://root:{os.getenv('PASSWORD')}@localhost:3306/hotel"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    api=Api(app)
    db.init_app(app)
    migrate=Migrate(app,db)

   


    api.add_resource(UserList ,"/users")
    api.add_resource(User, '/user/<string:username>')

    return app


