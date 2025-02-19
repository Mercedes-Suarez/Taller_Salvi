from backend.app import db

class UserType(db.Model):  # Nombre de la clase en PascalCase
    __tablename__ = 'user_type'

    id_user_type = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_type_name = db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self, user_type_name):
        self.user_type_name = user_type_name
