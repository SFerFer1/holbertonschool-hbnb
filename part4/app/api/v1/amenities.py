from flask_restx import Namespace, Resource, fields
from app.services import facade
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from flask_cors import CORS

api = Namespace('amenities', description='Amenity operations')
CORS(api)

# Define the amenity model for input validation and documentation
amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Name of the amenity')
})

@api.route('/')
class AmenityList(Resource):
    @api.expect(amenity_model)
    @api.response(201, 'Amenity successfully created')
    @api.response(400, 'Invalid input data')
    @jwt_required()
    def post(self):
        """Register a new amenity"""
        claims = get_jwt()
        if not claims.get('is_admin', True):
            return {'error': 'Admin privileges required'}, 403
        amenity_data = api.payload
        try:
            all_amenities = facade.get_all_amenities()
            for amenity in all_amenities:
                if amenity.name == amenity_data['name']:
                    return {"Error": "That amenitiy already exist"}, 400

            new_amenity = facade.create_amenity(amenity_data)
            return {'id': new_amenity.id, 'name': new_amenity.name}, 201
        except Exception as e:
            return {'error': {e}}, 400
            
    @api.response(200, 'List of amenities retrieved successfully')
    def get(self):
        """Retrieve a list of all amenities"""
        amenities = facade.get_all_amenities()
        return [{'id': amenity.id, 'name': amenity.name} for amenity in amenities], 200
    
@api.route('/<amenity_id>')
class AmenityResource(Resource):
    @api.response(200, 'Amenity details retrieved successfully')
    @api.response(404, 'Amenity not found')
    def get(self, amenity_id):
        """Get amenity details by ID"""
        amenity = facade.get_amenity(amenity_id)
        if not amenity:
            return  {'error': 'Amenity not found'}, 404
        return {'id': amenity.id, 'name': amenity.name}, 200

    @api.expect(amenity_model)
    @api.response(200, 'Amenity updated successfully')
    @api.response(404, 'Amenity not found')
    @api.response(400, 'Invalid input data')
    @jwt_required()
    def put(self, amenity_id):
        """Update an amenity's information"""
        amenity_data = api.payload
        amenity = facade.get_amenity(amenity_id)
        claims = get_jwt()
        if not claims.get('is_admin', True):
            return {'error': 'Admin privileges required'}, 403
        try:
            if not amenity:
                return {'error': 'Amenity not found'}, 404
        
            amenity = facade.update_amenity(amenity_id, amenity_data)
            return {'id': amenity.id, 'name': amenity.name}, 200
        except Exception as e:
            return {'error': '{e}'}, 400