from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    birth_date = db.Column(db.String(50))
    course = db.Column(db.String(50))
    phone = db.Column(db.Integer)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(50))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now()) 
