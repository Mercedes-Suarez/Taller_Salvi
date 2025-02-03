import os

class Config:
    # URL de conexión a MySQL (asegúrate de usar el nombre correcto de tu base de datos)
    SQLALCHEMY_DATABASE_URI = 'mysql://root:password@localhost/taller_salvi'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'mi_clave_secreta')