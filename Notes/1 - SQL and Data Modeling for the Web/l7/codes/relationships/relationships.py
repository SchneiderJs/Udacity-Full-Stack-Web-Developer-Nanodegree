from flask_sqlalchemy import SQLAlchemy

class Driver(db.Model):
    __tablename__ = "drivers"
    id = db.Column(db.Integer, primary_key=True)
    # ... Parent class ...
    vehicles = db.relationship('Vehicle', backref='driver', lazy=True)

class Vehicle(db.Model):
    __tablename__ = "vehicles"
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String, nullable=False)
    # ... Child class ... 
    vehicles_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'), nullable=False)
