from backend import db

class Advertisement(db.Model):
    __tablename__ = 'advertisements'

    id_advertisement = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_path = db.Column(db.String(255), nullable=False)
    contact = db.Column(db.String(100), nullable=False)
    publication_date = db.Column(db.DateTime, nullable=False)
    asset = db.Column(db.Integer, nullable=False)  # 1: Activo, 0: Inactivo
