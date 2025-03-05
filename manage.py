from backend import create_app
from backend.models import db
from flask_migrate import Migrate
from flask_script import Manager
from flask_migrate import MigrateComand

app = create_app()
migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(debug=True)