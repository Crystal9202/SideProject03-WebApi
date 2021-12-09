from Hotel import db
from Hotel.model.base  import Base



class StyleModel(Base):
    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String(60) , unique=True)
    rooms =db.relationship('RoomModel' ,back_populates = 'style')


    @staticmethod
    def get_style_list():
        return StyleModel.query.all()

    @staticmethod
    def get_by_name(name):
        return StyleModel.query.filter(StyleModel.name == name).first()




