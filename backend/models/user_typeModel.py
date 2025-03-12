from backend.models import db
from sqlalchemy.dialects.mysql import ENUM

class UserType(db.Model):
    __tablename__ = 'user_types'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_type_name = db.Column(
        ENUM('admin', 'mechanic', 'visitor', 'client'),
        unique=True,
        nullable=False
    )