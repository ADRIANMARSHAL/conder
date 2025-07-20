from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Crush(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    submitted_by = db.Column(db.String(100), nullable=False)
    instagram = db.Column(db.String(100), nullable=False)
