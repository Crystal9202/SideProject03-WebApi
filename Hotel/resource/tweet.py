from flask_restful import Resource ,reqparse
from Hotel.model.tweet import TweetModel
from Hotel.model.user import UserModel
from flask_jwt import jwt_required ,current_identity


class TweetList(Resource):
    def get(self):
        tweets = TweetModel.query.all()
        return [tweet.as_dict() for tweet in tweets]


class Tweet(Resource):
    @jwt_required()
    def get(self ,username):
        user = UserModel.get_by_name(username)
        if not user:
            return{'message':'user not found.'} ,404
        return [t.as_dict() for t in user.tweets]
        
    @jwt_required()
    def post(self ,username):
        if current_identity.username != username:
            return {'message' : 'Please use the right token'}
        parser = reqparse.RequestParser()
        parser.add_argument('body',type=str , help='body is required.' ,required=True)
        data = parser.parse_args()

        user=UserModel.get_by_name(username)
        if not user:
            {'message':'user not found.'},404

        tweet = TweetModel(user_id=user.id ,body=data['body'])
        tweet.add()
        return {'message':'post success'}