from flask import Blueprint, request, jsonify
from backend.services.appointmentsServices import (
    get_appointments_all, 
    get_appointment_by_id,
    create_appointment, 
    update_appointment, 
    delete_appointment
)
from backend.models import db

# Blueprint para Appointments
appointments_bp = Blueprint('appointments', __name__)

@appointments_bp.route('/appointments', methods=['GET'])
def get_appointments():
    try:
        aps = get_appointments_all()
    
        return jsonify([{ 
        "id": appt.id_appointment,        
        "vehicles_id": appt.id_vehicle,
        "appointment_date": appt.appointment_date.isoformat(),
        "state": appt.state,
        "notes": appt.notes,
       

    } for appt in aps])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@appointments_bp.route('/appoinments/<int:id>', methods=['GET'])
def get_appointment_by_id(id):
    try:
        appt = get_appointment_by_id(id)
        return jsonify({
            "id": appt.id_appointment,
            "vehicles_id": appt.id_vehicle,
            "appointment_date": appt.appointment_date.isoformat(),
            "state": appt.state,
            "notes": appt.notes,
          
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 404


@appointments_bp.route('/appointments', methods=['POST'])
def create_appointment():
    try:
        data = request.json
        new_apo = create_appointment(data)

        return jsonify({"message": "Appointment added", "id":new_apo.id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@appointments_bp.route('/appointments/<int:id>', methods=['PUT'])
def update_appointment_route(id, data):
    try:
        data = request.json
        update_appt = update_appointment(id,data)
        return jsonify({"message": "Appointment updated successfully"})
    except ValueError as ve:
        return jsonify({"error":str(ve)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@appointments_bp.route('/appointments/<int:id>', methods=['DELETE'])
def delete_appointment_route(id):
    try: 
        delete_appointment(id)
        return jsonify({"message": "Appointment deleted successfully"})
    except Exception as e:
        return jsonify({"error": "Appointment not found"}), 500
    