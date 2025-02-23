from backend import db

class Message(db.Model):
    __tablename__ = 'messages'

    id_message = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id_user'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message_text = db.Column(db.Text, nullable=False)
    shipping_date = db.Column(db.DateTime, nullable=False)
    state = db.Column(db.Enum('Pendiente', 'En gestión', 'Respondido'), nullable=False)
    response_text = db.Column(db.Text, nullable=True)
    response_date = db.Column(db.DateTime, nullable=True)