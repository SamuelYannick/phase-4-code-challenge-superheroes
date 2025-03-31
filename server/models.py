from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Hero(db.Model, SerializerMixin):
    __tablename__ = 'heroes'

    serialize_rules = ('-hero_powers.hero',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    super_name = db.Column(db.String)

    # Setting relationships
    hero_powers = db.relationship('HeroPower', back_populates='hero', 
                                  cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Hero {self.name}, {self.super_name}>'

class HeroPower(db.Model, SerializerMixin):
    __tablename__ = "hero_powers"

    serialize_rules = ('-hero.hero_powers', '-power.hero_powers',)

    id = db.Column(db.Integer, primary_key=True)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'))
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
    strength = db.Column(db.String)

    hero = db.relationship('Hero', back_populates='hero_powers')
    power = db.relationship('Power', back_populates='hero_powers')

    # def __init__(self, hero_id, power_id, strength):
    #     if strength not in ['Strong', 'Weak', 'Average']:
    #         raise ValueError("Invalid strength value. Must be 'Strong', 'Weak', or 'Average'")
    #     self.hero_id = hero_id
    #     self.power_id = power_id
    #     self.strength = strength

    def __repr__(self):
        return f'<HeroPowers {self.strength}>'

class Power(db.Model, SerializerMixin):
    __tablename__ = "powers"

    serialize_rules = ('-hero_powers.power',)

    description = db.Column(db.Text)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    hero_powers = db.relationship('HeroPower', back_populates='power',
                                  cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Power {self.name}, {self.description}'

