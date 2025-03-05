from backend.models import db

class UserType(db.Model):
    __tablename__ = 'user_type'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_type_name = db.Column(db.String(50), unique=True, nullable=False)

def initialize_roles():
    roles = ['admin', 'mechanic', 'visitor', 'client']

    for role in roles:
        if not UserType.query.filter_by(user_type_name=role).first():
            db.session.add(UserType(user_type_name=role))

    db.session.commit        
 