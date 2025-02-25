from base import Base
from email_validator import validate_email, EmailNotValidError

class User(Base):
    def __init__(self, first_name:str, last_name:str, email:str):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = False

    # Property to 'first_name'
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def fist_name(self, value):
        if len(value) > 50:
            raise ValueError("first name can not be longer than 50 characters")

    # Propery to 'last_name'
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def fistName(self, value):
        if len(value) > 50:
            raise ValueError("last name can not be longer than 50 characters")
        
    # Propery to 'email'
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, valor):
        try:
            validate_email(valor)
            self._email = valor
        except EmailNotValidError as error:
            raise ValueError(f'Error: {str(error)}')


    