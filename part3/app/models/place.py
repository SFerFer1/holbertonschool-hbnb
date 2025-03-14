#!/usr/bin/python3
from app.models.base import Base
from app.models.user import User
from app import db
from sqlalchemy.orm import validates

class Place(Base):
    __tablename__ = 'place'

    _title = db.Column(db.String(50), nullable=False)
    _description = db.Column(db.String(200), default=None)
    _price = db.Column(db.Integer, nullable=False)
    _latitude = db.Column(db.Float, nullable=False)
    _longitude = db.Column(db.Float, nullable=False)



    def __init__(self, title, description, price, latitude, longitude, owner, amenities):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.reviews = []
        self.amenities = amenities

    

    
    @validates("_title")
    def title(self, value):
        if not value or len(value) > 100:
            raise ValueError("The title is required and must be a maximum of 100 characters.")
        self._title = value
        return value

    @validates("_price")
    def price(self, value):
        if value <= 0:
            raise ValueError("The price must be a positive value")
        self._price = value
        return value

    @validates("_latitude")
    def latitude(self, value):
        if not (-90.0 <= value <= 90.0):
            raise ValueError("Latitude must be in the range of -90.0 to 90.0")
        self._latitude = value
        return value
    
    @validates("_longitude")
    def longitude(self, value):
        if not (-180.0 <= value <= 180.0):
            raise ValueError("The length must be in the range -180.0 to 180.0")
        self._longitude = value
        return value
    
    @validates("_owner")
    def owner(self, value):
        if not isinstance(value, User):
            raise ValueError("The owner must be a valid instance of User")
        self._owner = value
        return value
    
    @validates("_description")
    def description(self, value):
        self._description = value
        return value

    def add_review(self, review):
        """Add a review to the place."""
        self._reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self._amenities.append(amenity)