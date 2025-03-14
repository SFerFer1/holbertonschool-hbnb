from app.models.base import Base
from email_validator import validate_email, EmailNotValidError
from app import db
from sqlalchemy.orm import validates

class User(Base):
    __tablename__ = 'users'

    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def __init__(self, first_name:str, last_name:str, email:str, password:str, is_admin: bool = False):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin 
        self.password = password


    @validates("_first_name")
    def validate_first_name(self, key, value):
        if len(value) > 50:
            raise ValueError("first name can not be longer than 50 characters")
        return value

    @validates("_last_name")
    def validate_last_name(self, key, value):
        if len(value) > 50:
            raise ValueError("last name can not be longer than 50 characters")
        return value

    @validates("_email")
    def validate_email(self, key, value):
        try:
            t = validate_email(value, check_deliverability=False)
            self._email = t.normalized
        except EmailNotValidError as e:
            raise ValueError(f"Invalid email: {str(e)}")
        return value
    

    @validates('password') 
    def validate_password(self, key, password):
        """Hashes the password before storing it."""
        from app import bcrypt
        self._password = bcrypt.generate_password_hash(password).decode('utf-8')
        return self._password
    

    def verify_password(self, password):
        """Verifies if the provided password matches the hashed password."""
        from app import bcrypt
        return bcrypt.check_password_hash(self._password, password)