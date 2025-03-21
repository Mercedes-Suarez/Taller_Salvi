from backend.models import db
from backend.models.appointmentsModel import Appointment

def get_appointments_all():
    """Obtiene todas las citas"""
    return Appointment.query.all()

def get_appointment_by_id(appointment_id):
    """Obtiene una cita por ID"""
    return Appointment.query.get_or_404(appointment_id)

def create_appointment(data):
    """Crea uns nueva cita"""
    new_appt = Appointment(
        vehicles_id=data['id_vehicle'],
        appointment_date=data['appointment_date'],
        state=data['state'],
        notes=data['notes', ""],
  )
    db.session.add(new_appt)
    db.session.commit()
    return new_appt

def update_appointment(appointment_id, data):
    """Actualiza una cita"""
    appt = Appointment.query.get_or_404(appointment_id)

    required_fields = ['vehicle', 'appointment_date', 'state', 'notes', 'clients_id']

    for field in required_fields:
        if field not in data or not isinstance(data[field], str) or not data[field].strip():
            raise ValueError(f"{field} is required")
        
    appt.id_vehicle = data.get('id_vehicle', appt.id_vehicles)    
    appt.appointment_date = data.get('appointment_date', appt.appointment_date)
    appt.state = data.get('state', appt.state)
    appt.notes = data.get('notes', appt.notes)
    
    db.session.commit()
    return appt

def delete_appointment(appointment_id):
    """Elimina una cita"""
    appt = Appointment.query.get_or_404(appointment_id)
    db.session.delete(appt)
    db.session.commit()
    return appt

