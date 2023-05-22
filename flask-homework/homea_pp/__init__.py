from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from logging.config import dictConfig
from .config import AppConfig
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config.from_object(AppConfig)

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '%(levelname)s %(message)s',
    }}
})

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from .views import *
from .models import *

with app.app_context():
    db.create_all()
