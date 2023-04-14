from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from logging.config import dictConfig
from .config import AppConfig

app = Flask(__name__)
app.config.from_object(AppConfig)

db = SQLAlchemy(app)

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '%(levelname)s %(message)s',
    }}
})

from .views import *
from .models import *

with app.app_context():
    db.create_all()
