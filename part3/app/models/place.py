#!/usr/bin/python3
from app.models.base import Base
from app.models.user import User
from app import db
from sqlalchemy.orm import validates
from sqlalchemy.dialects.postgresql import UUID 
from sqlalchemy import ForeignKey


class Amenity_place(Base):
    __tablename__ = 'place_amenities'
    id_place = db.Column(UUID(as_uuid=True), ForeignKey('place.id'), primary_key=True)
    id_amenity = db.Column(UUID(as_uuid=True), ForeignKey('amenity.id'), primary_key=True)


class Place(Base):
    __tablename__ = 'place'

    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), default=None)
    price = db.Column(db.Integer, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    owner_id = db.Column(UUID(as_uuid=True), ForeignKey('user.id'), nullable=False)

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

    

    
    @validates("title")
    def validate_title(self, key, value):
        if not value or len(value) > 100:
            raise ValueError("The title is required and must be a maximum of 100 characters.")
        return value

    @validates("price")
    def validate_price(self, key, value):
        if value <= 0:
            raise ValueError("The price must be a positive value")
        return value

    @validates("latitude")
    def validate_latitude(self, key, value):
        if not (-90.0 <= value <= 90.0):
            raise ValueError("Latitude must be in the range of -90.0 to 90.0")
        return value
    
    @validates("longitude")
    def validate_longitude(self, key, value):
        if not (-180.0 <= value <= 180.0):
            raise ValueError("The length must be in the range -180.0 to 180.0")
        return value
    
    @validates("owner")
    def validate_owner(self, key, value):
        if not isinstance(value, User):
            raise ValueError("The owner must be a valid instance of User")
        return value
    
    @validates("description")
    def validate_description(self, key, value):
        return value

    def add_review(self, review):
        """Add a review to the place."""
        self._reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self._amenities.append(amenity)