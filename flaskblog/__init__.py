from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import dotenv_values
from flask_migrate import Migrate

config = dotenv_values(".env")
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config["POSTGRES_DATABASE"]
db = SQLAlchemy(app)
migrate = Migrate(app,db,compare_type=True)

from flaskblog import routes