from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Restaurant

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza_restaurants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = True

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

class Restaurants(Resource):
    def get(self):
        restaurants_dict = [restaurant.to_dict() for restaurant in Restaurant.query.all()]

        response = make_response(
            jsonify(restaurants_dict),
            200
        )
        return response

api.add_resource(Restaurants,'/restaurants')   



if __name__ == '__main__':
    app.run(port=5555, debug=True)