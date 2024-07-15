import time
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from sqlalchemy.exc import OperationalError

db = SQLAlchemy()

def init_db(app):
    with app.app_context():
        db.create_all()