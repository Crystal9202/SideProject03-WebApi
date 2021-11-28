from flask_restful import Resource ,reqparse ,abort,request
from flask import current_app
import jwt
from Hotel import db
from Hotel.model.user import UserModel 



class UserList(Resource):
    def get(self):
        token=request.headers.get('Authorization')
        try:
            jwt.decode(
                token,
                current_app.config.get('SECRET_KEY'),
                algorithms="HS256"
            )
        except jwt.ExpiredSignatureError:
            # the token is expired, return an error string
            return {"message": "Expired token. Please to get a new token."}
        except jwt.InvalidTokenError:
            # the token is invalid, return an error string
            return {"message": "Invalid token. Please register or login."}

        users=UserModel.query.all()
        return [user.as_dict() for user in users]

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username" ,type=str , help ="username is required." ,required=True)
        parser.add_argument("password" ,type=str , help ="password is required." ,required=True)
        parser.add_argument("email" ,type=str , help="email is required." ,required=True)
        data = parser.parse_args()

        user_find = None
        user = UserModel.query.filter(UserModel.username == data['username']).first()
        
        if user : 
            return abort(409, message="username already exists." )
        user = UserModel(username=data['username']  , email=data['email'])
        user.set_password(data['password'])
        db.session.add(user)
        db.session.commit()

        return user.as_dict() ,201

class User(Resource):
    def get(self,username):
        user=UserModel.query.filter(UserModel.username == username).first()
        if not user:
            return abort(404 , message='user not found')
        return user.as_dict()

    def put(self,username):
        parser = reqparse.RequestParser()
        parser.add_argument("password" ,type=str , help="password is required." ,required=True)
        parser.add_argument("email" ,type=str , help="email is required." ,required=True)
        data = parser.parse_args()

        user=UserModel.query.filter(UserModel.username == username).first()
        if user:
            user.set_password(data['password'])
            user.email=data['email']
            db.session.commit()
            return user.as_dict()
        user=UserModel(username=username , email=data['email'])
        user.set_password(data['password'])
        db.session.add(user)
        db.session.commit()
        return user.as_dict() , 201
        

    def patch(self,username):
        parser = reqparse.RequestParser()
        parser.add_argument("password" ,type=str )
        parser.add_argument("email" ,type=str )
        data = parser.parse_args()

        user=UserModel.query.filter(UserModel.username == username).first()

        if not user:
            abort(404, message="user not found")
        if data['password']:
            user.set_password(data['password'])
        if data['email']:
            user.email=data['email']
        db.session.commit()
        return user.as_dict()


    def delete(self,username):
        user=UserModel.query.filter(UserModel.username == username).first()
        if not user:
            abort(404 ,mseeage="user not found")
        
        db.session.delete(user)
        db.session.commit()
        return "",204