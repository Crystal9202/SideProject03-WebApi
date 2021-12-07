from Hotel import db
from Hotel.model.base  import Base



class StyleModel(Base):
    id = db.Column(db.Integer , primary_key = True)
    style = db.Column(db.String(60) , unique=True)
    rooms =db.relationship('RoomModel' ,back_populates = 'style')





