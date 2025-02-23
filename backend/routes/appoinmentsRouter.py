from flask import Blueprint, request, jsonify
from backend import db
from backend.models.appointmentsModel import Appointment

# Blueprint para Appointments
appointments_bp = Blueprint('appointments', __name__)

@appointments_bp.route('/appointments', methods=['GET'])
def get_appointments():
    appointments = Appointment.query.all()
    return jsonify([{ 
        "id_appointment": appt.id_appointment,
        "id_client": appt.id_client,
        "id_vehicle": appt.id_vehicle,
        "appointment_date": appt.appointment_date.isoformat(),
        "state": appt.state,
        "notes": appt.notes
    } for appt in appointments])

@appointments_bp.route('/appointments', methods=['POST'])
def create_appointment():
    data = request.json
    new_appointment = Appointment(
        id_client=data['id_client'],
        id_vehicle=data['id_vehicle'],
        appointment_date=data['appointment_date'],
        state=data['state'],
        notes=data['notes']
    )
    db.session.add(new_appointment)
    db.session.commit()
    return jsonify({"message": "Appointment added"}), 201

@appointments_bp.route('/appointments/<int:id>', methods=['PUT'])
def update_appointment(id):
    appointment = Appointment.query.get(id)
    if not appointment:
        return jsonify({"error": "Appointment not found"}), 404
    
    data = request.json
    appointment.appointment_date = data.get('appointment_date', appointment.appointment_date)
    appointment.state = data.get('state', appointment.state)
    appointment.notes = data.get('notes', appointment.notes)
    
    db.session.commit()
    return jsonify({"message": "Appointment updated successfully"})

@appointments_bp.route('/appointments/<int:id>', methods=['DELETE'])
def delete_appointment(id):
    appointment = Appointment.query.get(id)
    if not appointment:
        return jsonify({"error": "Appointment not found"}), 404
    
    db.session.delete(appointment)
    db.session.commit()
    return jsonify({"message": "Appointment deleted successfully"})