from flask_restx import Namespace, Resource, fields
from app.services import facade
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt


api = Namespace('places', description='Place operations')


# Define the models for related entities
amenity_model = api.model('PlaceAmenity', {
    'id': fields.String(description='Amenity ID'),
    'name': fields.String(description='Name of the amenity')
})

user_model = api.model('PlaceUser', {
    'id': fields.String(description='User ID'),
    'first_name': fields.String(description='First name of the owner'),
    'last_name': fields.String(description='Last name of the owner'),
    'email': fields.String(description='Email of the owner')
})

review_model = api.model('Review', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
    'user_id': fields.String(required=True, description='ID of the user'),
    'place_id': fields.String(required=True, description='ID of the place')
    })

# Define the place model for input validation and documentation
place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place'),
    'owner_id': fields.String(required=True, description='ID of the owner'),
    'amenities': fields.List(fields.String, required=True, description="List of amenities ID's"),
    'reviews': fields.List(fields.Nested(review_model), description='List of reviews')
})

@api.route('/')
class PlaceList(Resource):
    @jwt_required()
    @api.expect(place_model)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new place"""
        current_user = get_jwt_identity()
        place_data = api.payload
        if place_data['owner_id'] != current_user:
            return {'error': 'Unauthorized action'}, 403
        
        user = facade.get_user(place_data['owner_id'])

        for place in facade.get_all_places():
            if place_data['title'] == place.title:
                return {'error': 'place already exists'}, 400

        if not user:
            return {'error': 'user not found'}, 404

        place_data.pop('owner_id')
        place_data['owner'] = user
        new_place = facade.create_place(place_data)
        return {
            "id": new_place.id,
            "title": new_place.title,
            "description": new_place.description,
            "price": new_place.price,
            "latitude": new_place.latitude,
            "longitude": new_place.longitude,
            "owner_id": new_place.owner.id
            }, 201

    @api.response(200, 'List of places retrieved successfully')
    def get(self):
        """Retrieve a list of all places"""
        # Placeholder for logic to return a list of all places
        all_places = facade.get_all_places()
        all_reviews = facade.get_all_reviews()
        return [
            {
                'id': place.id,
                'title': place.title,
                'v': place.price,
                'price': place.price,
                'latitude': place.latitude,
                'longitude': place.longitude,
                'reviews': [
                    {
                        'text': review.text,
                        'rating': review.rating,
                        'user_id': review.user.id
                    }
                    for review in all_reviews
                    if review.place.id == place.id
                ]
            }
            for place in all_places
        ], 200

@api.route('/<place_id>')
class PlaceResource(Resource):
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get place details by ID"""
        place = facade.get_place(place_id)
        if not place:
            return {'error': 'Place not found'}, 404
        
        owner = place.owner
        if not owner:
            return {'error': 'Owner not found'}, 404

        amenities = facade.amenity_repo.get_all()
        ret = {
            'id': place.id,
            'title': place.title,
            'description': place.description,
            'latitude': place.latitude,
            'longitude': place.longitude,
            'owner': {
                'id': owner.id,
                'first_name': owner.first_name,
                'last_name': owner.last_name,
                'email': owner.email
            },
            'amenities': [{
                'id': amenity.id,
                'name': amenity.name
            } for amenity in amenities if amenity.place_id == place.id]
        }
        return ret, 200
    @api.expect(place_model)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input data')
    @jwt_required()
    def put(self, place_id):
        """Update a place's information"""
        
        current_user = jwt_required()
        data = api.payload
        

        place = facade.place_repo.get(place_id)

        claims = get_jwt()
        if claims.get('is_admin', True):
            pass
        elif place.owner.id != current_user:
            return {'error': 'Unauthorized action'}, 403

        if not place:
            return {"error": "Place not found"}, 404
        

        updated_place = facade.update_place(place_id, data)
        if not updated_place:
            return {"error": "Place updated fail"}, 404
        return {"message": "Place updated successfully"}, 200