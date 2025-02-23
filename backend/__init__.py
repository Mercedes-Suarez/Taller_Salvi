from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from backend.config import config

# Importar Blueprints de las rutas

from backend.routes.user_typeRoutes import user_type_bp
from backend.routes.spare_parts_inventoryRoutes import spare_parts_bp

db = SQLAlchemy()
migrate = Migrate()

def create_app():

    app = Flask(__name__)
    app.config.from_object(config['development'])

    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)

    # Registrar Blueprints

    app.register_blueprint(user_type_bp, url_prefix='/api')
    app.register_blueprint(spare_parts_bp, url_prefix='/api')
    

    @app.route("/")
    def home():
       return {"message": "API Taller Salvi funcionando"}
    
    return app