from flask_restx import Namespace, Resource, fields
from app.services import facade
from flask_jwt_extended import jwt_required, get_jwt_identity

api = Namespace('reviews', description='Review operations')

# Define the review model for input validation and documentation
review_model = api.model('Review', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
    'user_id': fields.String(required=True, description='ID of the user'),
    'place_id': fields.String(required=True, description='ID of the place')
})

@api.route('/reviews')
class ReviewList(Resource):
    @api.expect(review_model)
    @api.response(201, 'Review successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new review"""
        current_user = jwt_required()
        review_data = api.payload
        
        reviews_of_place = facade.get_reviews_by_place(review_data['place_id'])
        for review_inside_place in reviews_of_place:
            if current_user == review_inside_place.id:
                return {'error': 'You have already reviewed this place.'}, 400

        if current_user == review_data['user_id']:
            return {'error': "You cannot review your own place."}, 400

        all_reviews = facade.get_all_reviews()

        for review in all_reviews:
            if review.user.id == review_data['user_id'] and review.place.id == review_data['place_id']:
                return {"Error": "Review already exist"}, 400
        
        user = facade.get_user(review_data['user_id'])
        if not user:
            return {"Error": "User not found"}, 404
        
        place = facade.get_place(review_data['place_id'])
        if not place:
            return {"Error": "Place not found"}, 404
        
        review_data.pop('user_id')
        review_data.pop('place_id')

        review_data['user'] = user
        review_data['place'] = place

        new_review = facade.create_review(review_data)
        return {'id': new_review.id,
                 'text': new_review.text,
                   'rating': new_review.rating,
                     'user_id': user.id, 'place': place.id}, 201
    @api.response(200, 'List of reviews retrieved successfully')
    def get(self):
        """Retrieve a list of all reviews"""
        all_review = facade.get_all_reviews()
        return [{'id': review.id,
                  'text': review.text,
                    'rating': review.rating} for review in all_review], 200

@api.route('/reviews/<review_id>')
class ReviewResource(Resource):
    @api.response(200, 'Review details retrieved successfully')
    @api.response(404, 'Review not found')
    def get(self, review_id):
        """Get review details by ID"""
        # Placeholder for the logic to retrieve a review by ID
        review = facade.get_review(review_id)
        if not review:
            return {'Error': 'Review not found'}, 404
        return {'id': review.id, 'text': review.text, 'rating': review.rating, 'user_id': review.user.id, 'place': review.place.id}, 200


    @api.expect(review_model)
    @api.response(200, 'Review updated successfully')
    @api.response(404, 'Review not found')
    @api.response(400, 'Invalid input data')
    @jwt_required()
    def put(self, review_id):
        """Update a review's information"""
        current_user = get_jwt_identity()
        data = api.payload
        review = facade.get_review(review_id)

        if current_user != review.id:
            return {'error': 'Unauthorized action.'}, 403
        
        if review_id != current_user:
            return  {'Error': 'You cannot review your own place.'}, 400
        
        if not review:
            return {'Error': 'Review not found'}, 404
        
        update_review = facade.update_review(review_id, data)
        if not update_review:
            return {"error": "Review updated fail"}, 404
        return {"message": "Review updated successfully"}, 200

    @api.response(200, 'Review deleted successfully')
    @api.response(404, 'Review not found')
    @jwt_required()
    def delete(self, review_id):
        """Delete a review"""
        current_user = get_jwt_identity()
        if review_id != current_user:
            return {'error': 'Unauthorized action'}, 403


        review = facade.get_review(review_id)

        if not review:
            return {"error": "Review not found"}, 404
        review = facade.delete_review(review_id)
        return {"message": "Review deleted successfully"}, 200

@api.route('/places/<place_id>/reviews')
class PlaceReviewList(Resource):

    @api.response(200, 'List of reviews for the place retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get all reviews for a specific place"""
        place = facade.get_place(place_id)
        if not place:
            return {"error": "Place not found"}, 404
        reviews = facade.get_all_reviews()
        if not reviews:
            return {"error": "Reviews not found"}, 404
        return [{'id': review.id,
                'text': review.text,
                'rating': review.rating} for review in reviews if review.place.id == place_id], 200
