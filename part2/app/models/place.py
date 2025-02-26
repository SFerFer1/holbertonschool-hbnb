#!/usr/bin/python3
from app.models.base import Base
from app.models.user import User



class Place(Base):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.reviews = []
        self.amenities = []
    
    # Propiedad para 'title'
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if not value or len(value) > 100:
            raise ValueError("The title is required and must be a maximum of 100 characters.")
        self._title = value
    
    # Propiedad para 'price'
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("The price must be a positive value")
        self._price = value

    # Propiedad para 'latitude'
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        if not (-90.0 <= value <= 90.0):
            raise ValueError("Latitude must be in the range of -90.0 to 90.0")
        self._latitude = value

    # Propiedad para 'longitude'
    @property
    def longitude(self):
        return self._longitude
    
    @longitude.setter
    def longitude(self, value):
        if not (-180.0 <= value <= 180.0):
            raise ValueError("The length must be in the range -180.0 to 180.0")
        self._longitude = value

    # Propiedad para 'owner'
    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, value):
        if not isinstance(value, User):
            raise ValueError("The owner must be a valid instance of User")
        self._owner = value

    
    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)