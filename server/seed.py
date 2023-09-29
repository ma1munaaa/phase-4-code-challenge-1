from faker import Faker
from models import db, Restaurant, Pizza, Restaurant_pizzas
from app import app
import random

restaurant_names = [
    "Tasty Bites",
    "Food Fusion",
    "The Hungry Chef",
    "Sizzling Grill",
    "Cafe Delights",
    "Spice Heaven",
    "Bella Italia",
    "Thai Orchid",
    "Mama Mia Pizzeria",
    "Sushi Sake"
]
pizza_names = [
    "Margherita",
    "Pepperoni",
    "Supreme",
    "Hawaiian",
    "Vegetarian",
    "Meat Lovers",
    "BBQ Chicken",
    "Mushroom",
    "Sausage",
    "Buffalo Chicken",
    "White Pizza",
    "Pesto",
    "Pineapple",
    "Bacon",
    "Veggie Delight",
    "Four Cheese",
    "Chicken Alfredo",
    "Neapolitan",
    "Greek Pizza",
    "Taco Pizza",
]



with app.app_context():
    fake = Faker()

    Restaurant.query.delete()
    Pizza.query.delete()
    Restaurant_pizzas.query.delete()

    restaurants = []
    for restaurant in restaurant_names:
        new_restaurant = Restaurant(
            name = restaurant,
            address = fake.address()
        )
        restaurants.append(new_restaurant)
    db.session.add_all(restaurants)
    db.session.commit()
    print("Restaurants successfully populated")


    restaurant_pizzas = []
    for restaurant in Restaurant.query.all():
        random_pizza_count = random.randint(1,7)
        for i in range(random_pizza_count):
            new_restaurant_pizza = Restaurant_pizzas(
                pizza_id = random.randint(1,20),
                restaurant_id = restaurant.id,
                price = random.randint(1,30)
            )
            restaurant_pizzas.append(new_restaurant_pizza)
    db.session.add_all(restaurant_pizzas)
    db.session.commit()
    print("Restaurant Pizzas successfully populated")

