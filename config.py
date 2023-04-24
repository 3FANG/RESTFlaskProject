import pathlib

import connexion
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


basedir = pathlib.Path(__file__).parent.resolve()

app = connexion.FlaskApp(__name__, specification_dir=basedir)
app.add_api('swagger.yml')

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{basedir / 'people.db'}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)
ma = Marshmallow(app)



