from app.models.base import Base
from app.models.place import Place
from app.models.user import User
from app import db

class Review(Base):
    __tablename__ = 'reviews'

    _text = db.Column(db.String(50), nullable=False)
    _rating = db.Column(db.Integer, nullable=False)
    _latitude = db.Column(db.Float, nullable=False)



    def __init__(self, text, rating, user, place):
        super().__init__()
        self.text = text
        self.rating = rating
        self.user = user
        self.place = place
    
    @validates("_text")
    def text(self, value):
        if not value.strip():
            raise ValueError("El texto de la reseña no puede estar vacío.")
        self._text = value
        return value

    @validates("_rating")
    def rating(self, value):
        if not (1 <= value <= 5):
            raise ValueError("La calificación debe ser un número entre 1 y 5.")
        self._rating = value
        return value
   
    #falta hacer el validates para user, acordarse!!
    @user.setter
    def user(self, value):
        if not isinstance(value, User):
            raise ValueError("El usuario debe ser una instancia de la clase 'User'.")
        self._user = value

    #falta hacer el validates para place, acordarse!!
    @property
    def place(self):
        return self._place
    @place.setter
    def place(self, value):
        if not isinstance(value, Place):
            raise ValueError("El lugar debe ser una instancia de la clase 'Place'.")
        self._place = value