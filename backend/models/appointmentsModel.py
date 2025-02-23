from backend import db

class Appointment(db.Model):
    __tablename__ = 'appointments'

    id_appointment = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_client = db.Column(db.Integer, db.ForeignKey('clients.id_client'), nullable=False)
    id_vehicle = db.Column(db.Integer, nullable=False)  # Se puede hacer relación con una tabla de vehículos
    appointment_date = db.Column(db.DateTime, nullable=False)
    state = db.Column(db.Enum('Pendiente', 'Confirmada', 'Cancelada', 'Realizada'), nullable=False)
    notes = db.Column(db.Text, nullable=False)