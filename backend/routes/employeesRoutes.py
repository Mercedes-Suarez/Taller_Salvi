from flask import Blueprint, request, jsonify
from backend import db
from backend.models.employeesModel import Employee

# Blueprint para Employees
employees_bp = Blueprint('employees', __name__)

@employees_bp.route('/employees', methods=['GET'])
def get_employees():
    employees = Employee.query.all()
    return jsonify([{ 
        "id_employee": emp.id_employee,
        "id_user": emp.id_user,
        "name": emp.name,
        "phone": emp.phone,
        "email": emp.email,
        "address": emp.address,
        "post": emp.post,
        "date_start": emp.date_start.isoformat()
    } for emp in employees])

@employees_bp.route('/employees', methods=['POST'])
def create_employee():
    data = request.json
    new_employee = Employee(
        id_user=data['id_user'],
        name=data['name'],
        phone=data['phone'],
        email=data['email'],
        address=data['address'],
        post=data['post'],
        date_start=data['date_start']
    )
    db.session.add(new_employee)
    db.session.commit()
    return jsonify({"message": "Employee added"}), 201

@employees_bp.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    employee = Employee.query.get(id)
    if not employee:
        return jsonify({"error": "Employee not found"}), 404
    
    data = request.json
    employee.name = data.get('name', employee.name)
    employee.phone = data.get('phone', employee.phone)
    employee.email = data.get('email', employee.email)
    employee.address = data.get('address', employee.address)
    employee.post = data.get('post', employee.post)
    
    db.session.commit()
    return jsonify({"message": "Employee updated successfully"})

@employees_bp.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    employee = Employee.query.get(id)
    if not employee:
        return jsonify({"error": "Employee not found"}), 404
    
    db.session.delete(employee)
    db.session.commit()
    return jsonify({"message": "Employee deleted successfully"})