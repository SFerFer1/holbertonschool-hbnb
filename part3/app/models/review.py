from app.models.base import Base
from app.models.place import Place
from app.models.user import User
from app import db
from sqlalchemy.orm import validates, relationship
from sqlalchemy.dialects.postgresql import UUID 
from sqlalchemy import ForeignKey, Column, Table, Integer

class Review(Base):
    __tablename__ = 'review'

    text = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User', back_populates='reviews')
    place = relationship('Place', back_populates='reviews')
    place_id = Column(Integer, ForeignKey('place.id'), nullable=False)

    def __init__(self, text, rating, user, place):
        super().__init__()
        self.text = text
        self.rating = rating
        self.user = user
        self.place = place
        
    
    @validates("text")
    def validate_text(self, key, value):
        if not value.strip():
            raise ValueError("El texto de la reseña no puede estar vacío.")
        return value

    @validates("rating")
    def validate_rating(self, key, value):
        if not (1 <= value <= 5):
            raise ValueError("La calificación debe ser un número entre 1 y 5.")
        return value
