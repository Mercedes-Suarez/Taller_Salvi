from backend.models import db


class Client(db.Model):
    __tablename__ = 'clients'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    def get_user(self):
        from backend.models.usersModel import User
        return User.query.get(self.user_id)
    
    user = db.relationship('Users', backref=db.backref('clients', lazy=True))
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    address = db.Column(db.Text, nullable=False)
    register_date = db.Column(db.DateTime, nullable=False)