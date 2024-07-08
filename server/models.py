from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.types import DECIMAL

db = SQLAlchemy()

class Plant(db.Model, SerializerMixin):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    image = db.Column(db.String)
    price = db.Column(DECIMAL(db.Decimal))
    
    new_column = db.Column(db.String)
    db.create_all()
    def __repr__(self):
        return f'<Plant {self.name} | Price: {self.price}>'
    