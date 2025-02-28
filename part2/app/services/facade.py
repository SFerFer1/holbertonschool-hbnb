from app.models import User
from app.models import Amenity
from app.models import Review
from app.models import Place
from app.persistence.repository import InMemoryRepository

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()


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
            raise ValueError(f"Usuer not found.")

        if 'first_name' in user_data:
            user.first_name = user_data['first_name']
        if 'last_name' in user_data:
            user.last_name = user_data['last_name']
        if 'email' in user_data:
            user.email = user_data['email']

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
        place = self.place_repo[place_id]
        owner = place_data['owner']
        if not place:
             raise ValueError(f"Place not found")
        if 'owener' in place_data and  isinstance(place_data['owner'], User):
            place.owner = place_data[owner]
            
        if 'amenities' in place_data and isinstance(place_data['amenities'], list):
            if not all(isinstance(amenity, Amenity) for amenity in place_data['amenities']):
                raise TypeError("All elements in amenities must be  a Amenity.")



    def create_review(self, review_data):
        pass
    
    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
    # Placeholder for logic to retrieve all reviews for a specific place
        pass

    def update_review(self, review_id, review_data):
    # Placeholder for logic to update a review
        pass

    def delete_review(self, review_id):
    # Placeholder for logic to delete a review
        pass