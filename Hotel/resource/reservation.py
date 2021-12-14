from flask_restful import Resource ,reqparse
from flask_jwt import current_identity ,jwt_required
from Hotel.model.room import RoomModel
from Hotel.model.user import UserModel

class Reservation(Resource):
    @jwt_required()
    def get(self,username):
        if current_identity.username != username:
            return {'message':'Please use the right token.'}
        user = UserModel.get_by_name(username)
        if not user:
            return {'message':'User not found.'},404
        rooms = user.rooms
        return [room.as_dict() for room in rooms]

    @jwt_required()
    def put(self,username):
        if current_identity.username != username:
            return {'message':'Please use the right token.'}
        parser=reqparse.RequestParser()
        parser.add_argument('name',type=str ,help='name is required' ,required= True)
        data = parser.parse_args()

        user=UserModel.get_by_name(username)
        if not user:
           return {'message':'User not found.'},404

        room=RoomModel.get_by_name(data['name']) 
        if not room:
            return {'message':'Room not found.'},404
        if room.user_id_now:
            return {'message':'Room is not available.'}

        room.user_id_now = user.id
        room.update()

        return {'message': 'Your booking is confirmed.'}

    @jwt_required()
    def delete(self,username):
        if current_identity.username != username:
            return {'message':'Please use the right token.'}
            
        user=UserModel.get_by_name(username)
        if not user:
            return {'message':'User not found.'},404  

        rooms=user.rooms
        for room in rooms:
            room.user_id_now = None
            room.update()

        return {'message':'Cancel the reservation.'}

