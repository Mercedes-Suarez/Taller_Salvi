from backend import db

class UserType(db.Model):
    __tablename__ = 'user_type'

    id_user_type = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_type_name = db.Column(
        db.Enum('admin', 'mechanic', 'visitor', 'client', name="user_type_enum"),
        unique=True,
        nullable=False
    )

def initialize_roles():
    roles = ['admin', 'mechanic', 'visitor', 'client']

    for role in roles:
        if not UserType.query.filter_by(user_type_name=role).first():
            db.session.add(UserType(user_type_name=role))

db.session.commit()  