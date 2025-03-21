from backend.models import db
from backend.models.employeesModel import Employee
from datetime import datetime

def get_employees_all():
    """Obtiene todos los empleados de la base de datos."""
    return Employee.query.all()

def get_employee_by_id(employee_id):
    """Obtiene un empleado por su ID."""
    return Employee.query.get(employee_id)

def create_employee(data):
    """Crea un nuevo empleado en la base de datos."""
    if 'id_user' not in data or not isinstance(data['id_user'], int):
        raise ValueError("id_user must be an integer")

    required_fields = ['name', 'phone', 'email', 'address', 'post']
    for field in required_fields:
        if field not in data or not data[field].strip():
            raise ValueError(f"{field} is required and cannot be empty")

    date_start = datetime.fromisoformat(data['date_start']) if 'date_start' in data else datetime.utcnow()

    new_employee = Employee(
        id_user=data['id_user'],
        name=data['name'],
        phone=data['phone'],
        email=data['email'],
        address=data['address'],
        post=data['post'],
        date_start=date_start
    )
    db.session.add(new_employee)
    db.session.commit()
    return new_employee

def update_employee(employee_id, data):
    """Actualiza la información de un empleado existente."""
    employee = Employee.query.get(employee_id)
    if not employee:
        return None
    
    for field in ['name', 'phone', 'email', 'address', 'post']:
        if field in data and data[field].strip():
            setattr(employee, field, data[field])
    
    db.session.commit()
    return employee

def delete_employee(employee_id):
    """Elimina un empleado de la base de datos."""
    employee = Employee.query.get(employee_id)
    if not employee:
        return None
    
    db.session.delete(employee)
    db.session.commit()
    return employee