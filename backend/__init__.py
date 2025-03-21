from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from backend.config import config


from backend.models import db

migrate = Migrate()

def create_app():

    app = Flask(__name__)

   # Configuración de la base de datos
    app.config.from_object(config['development'])
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@127.0.0.1/Taller_Salvi'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Inicializar base de datos con la app
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)

    # Registrar Blueprints
    from backend.routes.user_typeRoutes import user_type_bp
    from backend.routes.spare_parts_inventoryRoutes import spare_parts_bp
    from backend.routes.usersRoutes import users_bp
    from backend.routes.messagesRoutes import messages_bp
    from backend.routes.advertisementsRoutes import advertisements_bp
    from backend.routes.chat_messagesRoutes import chat_messages_bp
    from backend.routes.session_tokensRoutes import session_tokens_bp
    from backend.routes.employeesRoutes import employees_bp
    from backend.routes.clientsRoutes import clients_bp
    from backend.routes.vehiclesRoutes import vehicles_bp
    from backend.routes.appointmentsRoutes import appointments_bp
    from backend.routes.repair_orderRoutes import repair_order_bp
    from backend.routes.repair_detailRoutes import repair_detail_bp
    from backend.routes.invoicesRoutes import invoices_bp
    from backend.routes.paymentsRoutes import payments_bp

    app.register_blueprint(user_type_bp, url_prefix='/api')
    app.register_blueprint(spare_parts_bp, url_prefix='/api')
    app.register_blueprint(users_bp, url_prefix='/api')
    app.register_blueprint(messages_bp, url_prefix='/api')
    app.register_blueprint(advertisements_bp, url_prefix='/api')
    app.register_blueprint(chat_messages_bp, url_prefix='/api')
    app.register_blueprint(session_tokens_bp, url_prefix='/api')
    app.register_blueprint(employees_bp, url_prefix='/api')
    app.register_blueprint(clients_bp, url_prefix='/api')
    app.register_blueprint(vehicles_bp, url_prefix='/api')
    app.register_blueprint(appointments_bp, url_prefix='/api')
    app.register_blueprint(repair_order_bp, url_prefix='/api')
    app.register_blueprint(repair_detail_bp, url_prefix='/api')
    app.register_blueprint(invoices_bp, url_prefix='/api')
    app.register_blueprint(payments_bp, url_prefix='/api')


    @app.route("/")
    def home():
       return {"message": "API Taller Salvi funcionando"}
    
    return app