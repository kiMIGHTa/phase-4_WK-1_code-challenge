from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource
from werkzeug.exceptions import NotFound

from models import db, Restaurant, RestaurantPizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza_restaurants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = True

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

class Restaurants(Resource):
    def get(self):
        restaurants = []
        for restaurant in Restaurant.query.all():
            restaurant_dict={
                "id": restaurant.id,
                "name": restaurant.name,
                "address":restaurant.address,
            }
            restaurants.append(restaurant_dict)

        response = make_response(
            jsonify(restaurants),
            200
        )
        return response

api.add_resource(Restaurants,'/restaurants') 

class RestaurantById(Resource):
    def get(self,id):
        restaurant = Restaurant.query.filter_by(id=id).first()
        if restaurant:
            restaurant_dict=restaurant.to_dict()
            response = make_response(
                jsonify(restaurant_dict),
                200
            )
            return response
        else:
            error_message = {"error": "Restaurant not found"}
            response = make_response(
                jsonify(error_message),
                404
            )
            return response
    def delete(self,id):

        restaurant = Restaurant.query.filter_by(id=id).first()
        restaurant_pizzas = RestaurantPizza.query.filter_by(restaurant_id=id).all()

        for restaurant_pizza in restaurant_pizzas:
            db.session.delete(restaurant_pizza)


        db.session.delete(restaurant)
        db.session.commit()


        response = make_response(
            "",
            200
        )
        return response
            


api.add_resource(RestaurantById,'/restaurants/<int:id>')



if __name__ == '__main__':
    app.run(port=5555, debug=True)