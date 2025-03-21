from flask import Blueprint, request, jsonify
from backend.services.employeesServices import (
    get_employees_all, get_employee_by_id,
    create_employee as create_employee_service,
    update_employee as update_employee_service,
    delete_employee as delete_employee_service
)

employees_bp = Blueprint('employees', __name__)

@employees_bp.route('/employees', methods=['GET'])
def get_employees():
    try:

      employees = get_employees_all()
      return jsonify([{ 
        "id_employee": emp.id_employee,
        "id_user": emp.id_user,
        "name": emp.name,
        "phone": emp.phone,
        "email": emp.email,
        "address": emp.address,
        "post": emp.post,
        "date_start": emp.date_start.isoformat() if emp.date_start else None
        } for emp in employees])
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@employees_bp.route('/employees/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    """Obtiene un empleado por su ID."""
    try:
        employee = get_employee_by_id(employee_id)
        if not employee:
            return jsonify({"error": "Employee not found"}), 404
        
        return jsonify({
            "id_employee": employee.id_employee,
            "id_user": employee.id_user,
            "name": employee.name,
            "phone": employee.phone,
            "email": employee.email,
            "address": employee.address,
            "post": employee.post,
            "date_start": employee.date_start.isoformat() if employee.date_start else None
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@employees_bp.route('/employees', methods=['POST'])
def create_employee():
    try:
        data = request.json
        new_employee = create_employee_service(data)
        return jsonify({"message": "Employee added", "id_employee": new_employee.id_employee}), 201
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@employees_bp.route('/employees/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    try:
        data = request.json
        updated_employee = update_employee_service(employee_id, data)
        if not updated_employee:
            return jsonify({"error": "Employee not found"}), 404
        
        return jsonify({"message": "Employee updated successfully"})
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@employees_bp.route('/employees/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    try:
        deleted_employee = delete_employee_service(employee_id)
        if not deleted_employee:
            return jsonify({"error": "Employee not found"}), 404
        
        return jsonify({"message": "Employee deleted successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500