from flask import Flask
from flask_restx import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


bcrypt = Bcrypt()

jwt = JWTManager()

def create_app(config_class="config.DevelopmentConfig"):
    app = Flask(__name__)
    app.url_map.strict_slashes = False

    #  Inicializamos bcrypt
    app.config.from_object(config_class)
    bcrypt.init_app(app)
    jwt.init_app(app)
    db.init_app(app)
    
    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API')
    from app.api.v1.users import api as users_ns
    from app.api.v1.amenities import api as amenities_api
    from app.api.v1.places import api as places_api
    from app.api.v1.auth import api as auth_api
    from app.api.v1.reviews import api as reviews_api

    with app.app_context():
        db.create_all()

    # Register the users namespace
    api.add_namespace(users_ns, path='/api/v1/users')
    api.add_namespace(amenities_api, path='/api/v1/amenities')
    api.add_namespace(places_api, path='/api/v1/places')
    api.add_namespace(auth_api, path='/api/v1/auth')
    api.add_namespace(reviews_api, path='/api/v1')

    return app



