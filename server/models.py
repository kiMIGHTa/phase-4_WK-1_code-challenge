from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Restaurant(db.Model,SerializerMixin):
    __tablename__ = 'restaurants'

    serialize_rules = ('-restaurant_pizzas.restaurant',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)    
    
    restaurant_pizzas=db.relationship('RestaurantPizza', backref='restaurant')

    def __repr__(self):
        return f'<Restaurant {self.name}| address: {self.address}'
    

class Pizza(db.Model,SerializerMixin):
    __tablename__ = 'pizzas'

    serialize_rules = ('-restaurant_pizzas.pizza',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ingredients = db.Column(db.String)    
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    restaurant_pizzas=db.relationship('RestaurantPizza', backref='pizza')


    def __repr__(self):
        return f'<Pizza {self.name}| ingredients: {self.ingredients}'
    
class RestaurantPizza(db.Model,SerializerMixin):
    __tablename__ = 'restaurant_pizzas'

    serialize_rules = ('-restaurant.restaurant_pizzas', '-pizza.restaurant_pizzas')


    id = db.Column(db.Integer, primary_key=True)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    price = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    restaurants=db.relationship('Restaurant', backref='restaurant_pizzas')
    pizzas=db.relationship('Pizza', backref='restaurant_pizzas')



    def __repr__(self):
        return f'<RestaurantPizza  price: {self.price}'    