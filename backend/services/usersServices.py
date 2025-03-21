from backend.models import db
from backend.models.usersModel import User
from werkzeug.security import generate_password_hash

def get_all_users():
    """Obtiene todos los usuarios."""
    return User.query.all()

def get_user_by_id(user_id):
    """Obtiene un usuario por su ID."""
    return User.query.get(user_id)

def create_user(data):
    """Crea un nuevo usuario."""
    new_user = User(
        username=data['username'],
        email=data['email'],
        password=generate_password_hash(data['password']),
        user_type_id=data['user_type_id']
    )
    db.session.add(new_user)
    db.session.commit()
    return new_user

def update_user(user_id, data):
    """Actualiza la información de un usuario."""
    user = User.query.get(user_id)
    if not user:
        return None

    user.username = data.get('username', user.username)
    user.email = data.get('email', user.email)
    user.password = generate_password_hash(data['password']) if 'password' in data else user.password
    user.user_type_id = data.get('user_type_id', user.user_type_id)
    
    db.session.commit()
    return user

def delete_user(user_id):
    """Elimina un usuario."""
    user = User.query.get(user_id)
    if not user:
        return None

    db.session.delete(user)
    db.session.commit()
    return user