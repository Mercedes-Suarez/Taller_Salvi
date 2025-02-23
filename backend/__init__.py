from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from backend.config import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():

    app = Flask(__name__)
    app.config.from_object(config['development'])

    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)

    @app.route("/")
    def home():
       return {"message": "API Taller Salvi funcionando"}
    
    return app