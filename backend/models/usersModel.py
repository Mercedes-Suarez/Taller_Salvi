from backend.models import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    user_type_id = db.Column(db.Integer, db.ForeignKey('user_types.id'), nullable=False)

    user_type = db.relationship('UserType', backref=db.backref('users', lazy='dynamic'))

    def __init__(self, username, email, password, user_type_id):
    
        self.username = username
        self.email = email
        self.password = password
        self.user_type_id = user_type_id  
        
    def get_employee(self):
        from backend.models.employeesModel import Employee  # Se importa dentro de la función
        return Employee.query.filter_by(user_id=self.id).first()             
