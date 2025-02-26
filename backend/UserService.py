from backend import db
from models.userModel import Users

class UserService:
    @staticmethod
    def get_all_users():
        return Users.query.all()

    @staticmethod
    def get_user_by_id(user_id):
        return Users.query.get(user_id)

    @staticmethod
    def create_user(name, email, password, user_type):
        new_user = Users(name=name, email=email, password=password, user_type=user_type)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def delete_user(user_id):
        user = Users.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False