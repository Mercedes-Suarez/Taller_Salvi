from backend import db
from backend.models.user_typeModel import UserType

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    user_type_id = db.Column(db.Integer, db.ForeignKey('user_types.id'), nullable=False)
    registration_date = db.Column(db.DateTime, server_default=db.func.now())

    user_type = db.relationship('UserType', backref=db.backref('users', lazy=True))

    def __init__(self, name, email, password, user_type_id):
    
        self.name = name
        self.email = email
        self.password = password
        self.user_type_id = user_type_id       
