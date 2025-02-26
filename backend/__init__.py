from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from backend.config import config

# Importar Blueprints de las rutas

from backend.routes.user_typeRoutes import user_type_bp
from backend.routes.spare_parts_inventoryRoutes import spare_parts_bp
from backend.routes.usersRoutes import user_bp
from backend.routes.messagesRoutes import messages_bp
from backend.routes.advertisementsRoutes import advertisements_bp
from backend.routes.chat_messagesRoutes import chat_messages_bp
from backend.routes.session_tokensRoutes import session_tokens_bp
from backend.routes.employeesRoutes import employees_bp
from backend.routes.clientsRoutes import clients_bp
from backend.routes.vehiclesRoutes import vehicles_bp
from backend.routes.appoinmentsRouter import appointments_bp
from backend.routes.repair_ordersRoutes import repair_orders_bp
from backend.routes.repair_detailsRoutes import repair_details_bp
from backend.routes.invoicesRoutes import invoices_bp
from backend.routes.paymentsRoutes import payments_bp

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
    app.register_blueprint(user_bp, url_prefix='/api')
    app.register_blueprint(messages_bp, url_prefix='/api')
    app.register_blueprint(advertisements_bp, url_prefix='/api')
    app.register_blueprint(chat_messages_bp, url_prefix='/api')
    app.register_blueprint(session_tokens_bp, url_prefix='/api')
    app.register_blueprint(employees_bp, url_prefix='/api')
    app.register_blueprint(clients_bp, url_prefix='/api')
    app.register_blueprint(vehicles_bp, url_prefix='/api')
    app.register_blueprint(appointments_bp, url_prefix='/api')
    app.register_blueprint(repair_orders_bp, url_prefix='/api')
    app.register_blueprint(repair_details_bp, url_prefix='/api')
    app.register_blueprint(invoices_bp, url_prefix='/api')
    app.register_blueprint(payments_bp, url_prefix='/api')


    @app.route("/")
    def home():
       return {"message": "API Taller Salvi funcionando"}
    
    return app