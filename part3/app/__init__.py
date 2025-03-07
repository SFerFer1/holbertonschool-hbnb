from flask import Flask
from flask_restx import Api
from app.api.v1.users import api as users_ns
from app.api.v1.amenities import api as amenities_api
from app.api.v1.places import api as places_api
from app.services.facade import HBnBFacade
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

bcrypt = Bcrypt()

facade = HBnBFacade()

jwt = JWTManager()

def create_app(config_class="config.DevelopmentConfig"):
    app = Flask(__name__)


    #  Inicializamos bcrypt
    app.config.from_object(config_class)
    bcrypt.init_app(app)
    
    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API')

    # Register the users namespace
    api.add_namespace(users_ns, path='/api/v1/users')
    api.add_namespace(amenities_api, path='/api/v1/amenities')
    api.add_namespace(places_api, path='/api/v1/places')
    return app


def create_app(config_class=config.DevelopmentConfig):
     #
     # Existent code with app Flask instance
     # ...
    jwt.init_app(app)
