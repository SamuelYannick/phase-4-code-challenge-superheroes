#!usr/bin/env python3

from flask import Flask, request, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db, Hero, HeroPower, Power

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/')
def index():
    return "Index for Superheroes API"

@app.route('/heroes')
def get_heroes():
    heroes = [hero.to_dict() for hero in Hero.query.all()] # could use hero = Hero.query.get(id) => works still, more concise

    return make_response(heroes, 200)

@app.route('/heroes/<int:id>')
def hero_by_id(id):
    hero = Hero.query.filter(Hero.id == id).first()
    if not hero:
        return make_response({"error": "Hero not found"}, 404)

    return make_response(hero.to_dict(), 200)

@app.route('/powers')
def get_powers():
    powers = [power.to_dict() for power in Power.query.all()]

    return make_response(powers, 200)

@app.route('/powers/<int:id>', methods=['GET', 'PATCH'])
def power_by_id(id):
    power = Power.query.filter(Power.id == id).first()
    if not power:
        return make_response({"error": "Power not found"}, 404)

    # if request.method == 'GET':
    #     return make_response(power.to_dict(), 200)
    
    if request.method == 'PATCH':
        data = request.get_json()
        new_description = data.get_json('decription')
        if not new_description or len(new_description) < 20 or new_description == power.description:
            return make_response({"errors": ["Description must be at least 20 characters long"]}, 400)

        power.description = new_description
        db.session.commit()

    return make_response(power.to_dict(), 200)

@app.route('/hero_powers', methods=['POST'])
def new_hero_power():
    data = request.get_json()

    hero_id = data.get('hero_id')
    power_id = data.get('power_id')
    strength = data.get('strength')

    if strength not in ['Strong', 'Weak', 'Average']:
        return make_response({"errors": ["Strength must be 'Strong', 'Weak', or 'Average'"]}, 400)
    
    hero = Hero.query.get(hero_id)
    power = Power.query.get(power_id)

    if not hero or not power:
        return make_response({"errors": ["Hero or Power not found"]}, 404)
    
    hero_power = HeroPower(hero_id=hero_id, power_id=power_id, strength=strength)
    db.session.add(hero_power)
    db.session.commit()

    return make_response(hero_power.to_dict(), 201)


if __name__ == "__main__":
    app.run(port=5555, debug=True)