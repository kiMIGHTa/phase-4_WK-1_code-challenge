from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource
from werkzeug.exceptions import NotFound

from models import db, Restaurant, RestaurantPizza, Pizza

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
        if restaurant:
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
        else:
            error_message = {"error": "Restaurant not found"}
            response = make_response(
                jsonify(error_message),
                404
            )
            return response

api.add_resource(RestaurantById,'/restaurants/<int:id>')


class Pizzas(Resource):
    def get(self):
        pizzas = []
        for pizza in Pizza.query.all():
            pizza_dict={
                "id": pizza.id,
                "name": pizza.name,
                "ingredients":pizza.ingredients,
            }
            pizzas.append(pizza_dict)

        response = make_response(
            jsonify(pizzas),
            200
        )
        return response

api.add_resource(Pizzas,'/pizzas') 

class RestaurantPizzas(Resource):
    def post(self):
        data=request.get_json()

        price = data['price']
        pizza_id = data['pizza_id']
        restaurant_id = data['restaurant_id']

        # if not (price and pizza_id and restaurant_id):
        #         return jsonify({"errors": ["Validation errors"]}), 400


    # Create a new RestaurantPizza instance
        new_restaurant_pizza = RestaurantPizza(
            price=price,
            pizza_id=pizza_id,
            restaurant_id=restaurant_id
        )
        db.session.add(new_restaurant_pizza)
        db.session.commit()

        pizza = Pizza.query.filter_by(id=pizza_id).first()
        pizza_dict = {
                "id": pizza.id,
                "name": pizza.name,
                "ingredients":pizza.ingredients,
            }
        response = make_response(
            jsonify(pizza_dict),
            201
        )
        return response
    
api.add_resource(RestaurantPizzas,'/restaurant_pizzas')    




if __name__ == '__main__':
    app.run(port=5555, debug=True)