#!/usr/bin/env python3

from app import app
from models import db, Restaurant, Pizza, RestaurantPizza

with app.app_context():

    Restaurant.query.delete()
    Pizza.query.delete()
    RestaurantPizza.query.delete()

    dominion = Restaurant(
        id = 1,
        name = "Dominion Pizza",
        address = "Good Italian, Ngong Road, 5th Avenue"
    )

    pizza_hut = Restaurant(
        id=2,
        name="Pizza Hut",
        address="Westgate Mall, Mwanzi Road, Nrb 100",
    )

    pizza_inn = Restaurant(
        id=3,
        name="Pizza Inn",
        address="Kahawa Sukari",
    )

    db.session.add_all([dominion, pizza_hut])
    db.session.commit()

    cheese = Pizza(
        id=1,
        name="Cheese",
        ingredients="Dough, Tomato Sauce, Cheese",
    )

    pepperoni = Pizza(
        id=2,
        name="Pepperoni",
        ingredients="Dough, Tomato Sauce, Cheese, Pepperoni",
    )

    db.session.add_all([cheese, pepperoni])
    db.session.commit()

    offers = RestaurantPizza(
        price=200,
        pizza_id=2,
        restaurant_id=1
    )
    offers2 = RestaurantPizza(
        price=200,
        pizza_id=1,
        restaurant_id=1
    )

    db.session.add_all([offers,offers2])
    db.session.commit()

