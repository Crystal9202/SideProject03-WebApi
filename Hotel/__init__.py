
from flask import Flask
from flask_restful import Api, Resource ,reqparse ,abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



db=SQLAlchemy()
from Hotel.model.user  import UserModel 
from Hotel.resource.user import UserList , User 
from Hotel.resource.auth import Login
from Hotel.config import Config



def create_app():   #工廠函數
    app=Flask('Hotel')
    app.config.from_object(Config)
    api=Api(app)
    db.init_app(app)
    migrate=Migrate(app,db)


    api.add_resource(UserList ,"/users")
    api.add_resource(User, '/user/<string:username>')
    api.add_resource(Login ,'/auth/login')
    return app


