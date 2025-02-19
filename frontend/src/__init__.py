from flask import Flask
from config import DevelopmentConfig

app = Flask(__name__)

app.config.from_object(DevelopmentConfig)

def init_app():
    return app