This project is a clone of Airbnb called HBnB.

The organization of the project is as follows:

hbnb/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── users.py
│   │       ├── places.py
│   │       ├── reviews.py
│   │       └── amenities.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── place.py
│   │   ├── review.py
│   │   └── amenity.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── facade.py
│   └── persistence/
│       ├── __init__.py
│       └── repository.py
├── run.py
├── config.py
├── requirements.txt
└── README.md

Description of Layers

Presentation:
Responsible for user interaction through the API. It uses Flask and Flask-RESTx to define routes and handle HTTP requests.

Business Logic:
Contains the core rules and processes of the system. This is where the classes and methods are defined to manage the creation, update, and processing of user, place, review, and amenity.

Persistence:
An in-memory repository is used for storing and validating objects. This layer is designed to be replaceable in the future.

Facade:
The Facade pattern is implemented in the service layer to simplify interaction between the different layers of the system. This is where processes like creation and deletion are handled, which will be used in the API.

Clasess:
Main Entities

Amenity
This class represents an "amenity," which is something extra that a place offers (like Wi-Fi, a pool, a gym, etc.). Here are the responsibilities and details:

Properties:

name: The name of the amenity, which must be a maximum of 50 characters. If it's empty or too long, it raises an error.
Responsibilities:

Ensures that the amenity name is valid before saving it.
Place
A Place is essentially a location that can be rented, like a property. Here's what's important:

Properties:

title: The title of the place. It cannot be longer than 100 characters.
description: A description of the place.
price: The rental price. It must be a positive number.
latitude and longitude: The coordinates of the place. They need to be in the correct range.
owner: The owner of the place, which must be an object of type User.
reviews: The reviews given to the place.
amenities: The amenities that the place has.
Responsibilities:

Ensures that all data is valid before saving anything.
Can add reviews and amenities to a place.
Review
The Review class is for the reviews of places. A user can leave their opinion about a place, and these are the properties:

Properties:

text: The text of the review. It cannot be empty.
rating: The rating of the place, which must be between 1 and 5.
place: The place to which the review belongs. It must be a Place object.
user: The user who wrote the review. It must be a User object.
Responsibilities:

Validates that the review text is not empty and that the rating is between 1 and 5.
Ensures that both the place and the user are valid.
User
The User class is for the system's users, who can be owners, guests, or others. Here are their properties:

Properties:

first_name: The user's first name. It cannot be longer than 50 characters.
last_name: The user's last name. It also has a 50-character limit.
email: The user's email address.
is_admin: Whether the user is an administrator. By default, it's False.
Responsibilities:

Ensures that user data is correct (such as name size and email).
Users can be owners of places or write reviews.
Summary

Data Validation:
Each class validates that the data is correct. If not, it raises an error.

Relationships:

A Place has an owner who is a User.
A Review is associated with a Place and a User.
Places can have multiple reviews and amenities, which are managed within their respective classes.
Update and Persistence:
The classes have methods to update attributes and keep everything organized.


test file:
test.py

Install requirements :
pip install -r requirements.txt

To execute the app use:
python run.py
