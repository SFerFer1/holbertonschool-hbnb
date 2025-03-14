#!/usr/bin/python3

from app.models.base import Base
from app import db

class Amenity(Base):
    __tablename__ = 'amenities'

    _name = db.Column(db.String(100), nullable=False)

    def __init__(self, name):
        super().__init__()  # Llama al constructor de Base (que maneja el ID y datetime)
        self.name = name

    # Propiedad para 'name'
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) > 50:
            raise ValueError("The name can be a maximum of 50 characters.")
        if not value:
            raise ValueError("the email can't be empty")
        self._name = value