from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return {"message": "API Taller Salvi funcionando"}

if __name__ == "__main__":
    app.run(debug=True, port=5000)
    