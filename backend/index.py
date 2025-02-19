from flask import Flask
from config import config

app = Flask(__name__)
app.config.from_objet(config['development'])
