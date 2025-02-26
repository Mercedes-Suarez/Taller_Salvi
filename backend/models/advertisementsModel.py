from backend import db

class Advertisement(db.Model):
    __tablename__ = 'advertisements'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_path = db.Column(db.String(255), nullable=False)
    contact = db.Column(db.String(100), nullable=False)
    publication_date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    is_active = db.Column(db.Boolean, nullable=False, default=True, server_default="1")  # 1: Activo, 0: Inactivo
    
