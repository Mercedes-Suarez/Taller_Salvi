from backend.models import db
from backend.models.sessionTokensModel import SessionToken
from datetime import datetime

def get_session_tokens_all():
    """Obtiene todos los tokens de sesión."""
    return SessionToken.query.all()

def get_session_token_by_id(token_id):
    """Obtiene un token de sesión por su ID."""
    return SessionToken.query.get(token_id)

def create_session_token(data):
    """Crea un nuevo token de sesión en la base de datos."""
    new_token = SessionToken(
        user_id=data['user_id'],
        token=data['token'],
        creation_date=datetime.fromisoformat(data['creation_date']) if 'creation_date' in data else datetime.utcnow(),
        expiration_date=datetime.fromisoformat(data['expiration_date'])
    )
    db.session.add(new_token)
    db.session.commit()
    return new_token

def update_session_token(token_id, data):
    """Actualiza un token de sesión existente."""
    token = SessionToken.query.get(token_id)
    if not token:
        return None

    token.token = data.get('token', token.token)
    token.expiration_date = datetime.fromisoformat(data['expiration_date']) if 'expiration_date' in data else token.expiration_date
    
    db.session.commit()
    return token

def delete_session_token(token_id):
    """Elimina un token de sesión de la base de datos."""
    token = SessionToken.query.get(token_id)
    if not token:
        return None

    db.session.delete(token)
    db.session.commit()
    return token