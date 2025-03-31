#!/usr/bin/python3

from app.models.base import Base
from app import db
from sqlalchemy.orm import validates, relationship
from app.models.place import place_amenities

class Amenity(Base):
    __tablename__ = 'amenity'

    name = db.Column(db.String(100), nullable=False)
    places = relationship('Place', secondary=place_amenities, back_populates='amenities')

    def __init__(self, name):
        super().__init__()  # Llama al constructor de Base (que maneja el ID y datetime)
        self.name = name


    @validates('name')
    def validate_name(self, key, value):
        if len(value) > 50:
            raise ValueError("The name can be a maximum of 50 characters.")
        if not value:
            raise ValueError("the email can't be empty")
        return value