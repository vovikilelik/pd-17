from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

DATABASE_PATH = 'res/database.db'

current_app = Flask('__main__')
current_app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DATABASE_PATH}"
current_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

current_api = Api(current_app)

current_db = SQLAlchemy(current_app)

