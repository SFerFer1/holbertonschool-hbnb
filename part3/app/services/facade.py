from app.models import User
from app.models import Amenity
from app.models import Review
from app.models import Place
from app.persistence.repository import InMemoryRepository, SQLAlchemyRepository

class HBnBFacade:
    def __init__(self):
        self.user_repo = SQLAlchemyRepository(User)
        self.amenity_repo = SQLAlchemyRepository(Amenity)
        self.review_repo = SQLAlchemyRepository(Review)
        self.place_repo = SQLAlchemyRepository(Place)

    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)
    
    def get_all_users(self):
        return self.user_repo.get_all()

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)
    
    def update_user(self, user_id, user_data):

        user = self.user_repo.get(user_id)
        if not user:
            raise ValueError(f"User not found.")

        if 'first_name' in user_data:
            user.first_name = user_data['first_name']
        if 'last_name' in user_data:
            user.last_name = user_data['last_name']
        if 'email' in user_data:
            user.email = user_data['email']
        if 'password' in user_data:
            user.password = user_data['email']

        self.user_repo.update(user, user_data)

        return user

    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.amenity_repo.get(amenity_id)
        if not amenity:
            raise ValueError(f"Amenity not found.")
        if 'name' in amenity_data:
            amenity.name = amenity_data['name']

        self.amenity_repo.update(amenity, amenity_data)
        return amenity
    
    def create_place(self, place_data):
        place = Place(**place_data)

        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        place = self.place_repo(place_id)
        owner = place_data['owner']

        if 'title' in place_data:
            place.title = place_data['title']
        
        if 'description' in place_data:
            place.description = place_data['description']
        
        if 'price' in place_data:
            place.price = place_data['price']
        
        if 'latitude' in place_data:
            place.latitude = place_data['latitude']
        
        if 'longitude' in place_data:
            place.longitude = place_data['longitude']

        if 'reviews' in place_data:
            place.reviews.append(place_data['reviews'])
        
        if 'amenities' in place_data:
            place.amenities.append(place_data['amenities'])

        return place
    def create_review(self, review_data):
        review = Review(**review_data)
        place = review_data['place']
        place.add_review(review)
        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
        return self.review_repo.get(review_id)
        

    def get_all_reviews(self):
        return self.review_repo.get_all()
        
    
    def get_reviews_by_place(self, place_id):
        place = self.get_place(place_id)
        return place.reviews

    def update_review(self, review_id, review_data):
        review_to_change = self.get_review(review_id)
        for place in self.get_all_places():
            for review in place.reviews:
                if review == review_to_change:
                    if 'text' in review_data:
                        review.text = review_data['text']

                    if 'rating' in review_data:
                        review.rating = review_data['rating']
        return f"{review_id} doesn´t match any review"


    def delete_review(self, review_id):
        try:
            self.place_repo.delete(review_id)
            self.review_repo.delete(review_id)
            return f"Review with ID {review_id} has been deleted."
        except: 
            return f"Review with ID {review_id} not found."
