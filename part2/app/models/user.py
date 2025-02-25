import uuid
from datetime import datetime

class User():
    def __init__(self, firstName, lastName, Email):
        self.id = str(uuid.uuid4())
        self.first_name = firstName
        self.last_name = lastName
        self.email = Email
        self.is_admin = False
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

       @User.setter
       def User(self, firstname, lastname, email, ):
           