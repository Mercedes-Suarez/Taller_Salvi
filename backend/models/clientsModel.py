from backend import db
from backend.models.usersModel import Users

class Client(db.Model):
    __tablename__ = 'clients'

    id_client = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id_user'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    address = db.Column(db.Text, nullable=False)
    register_date = db.Column(db.DateTime, nullable=False)

# Relación con Users
    user = db.relationship('Users', backref=db.backref('clients', lazy=True))