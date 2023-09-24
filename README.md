# phase-4_WK-1_code-challenge

## Author
- Author: Dennis Kimaita

## Technologies Used
- Python 3
- Flask
- Flask-SQLAlchemy
- SQLAlchemy
- SQLAlchemy-Serializer

## Description
- This is a simple Flask-based API for managing restaurants, pizzas, and their offers. 
- It allows you to create, read, update, and delete restaurants and pizzas, as well as associate pizzas with specific restaurants along with their prices.

  
The API will be available at `http://localhost:5000`.

## API Endpoints

### Restaurants

- **GET /restaurants**
- Description: Get a list of all restaurants.
- **GET /restaurants/{restaurant_id}**
- Description: Get details of a specific restaurant by ID.
- **DELETE /restaurants/{restaurant_id}**
- Description: Delete a specific restaurant by ID.

### Pizzas

- **GET /pizzas**
- Description: Get a list of all pizzas.


### Restaurant Pizzas (Offers)

- **GET /offers**
- Description: Get a list of all restaurant pizza offers.

- **POST /offers**
- Description: Create a new restaurant pizza offer.
- Payload: JSON data with restaurant ID, pizza ID, and price.




## Command Reference

- To start the Flask development server: `flask run`
- To create the database tables: `flask db upgrade`
- To run the database seeding script: `python seed.py`


