from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Crush(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    instagram = db.Column(db.String(150), nullable=False)
    submitted_by = db.Column(db.String(150), nullable=False)
