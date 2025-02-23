from backend import db

class Employee(db.Model):
    __tablename__ = 'employees'

    id_employee = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id_user'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    address = db.Column(db.Text, nullable=False)
    post = db.Column(db.Enum('Administrador', 'Mecánico'), nullable=False)
    date_start = db.Column(db.DateTime, nullable=False)