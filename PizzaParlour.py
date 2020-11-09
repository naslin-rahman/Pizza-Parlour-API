from flask import Flask, request
from Classes.parlourInterface import ParlourInterface
import json

app = Flask("Assignment 2")
parlour = ParlourInterface()

@app.route('/pizza')
def welcome_pizza():
    return 'Welcome to Pizza Planet!'

@app.route('/menu')
def menu():
    # Return the entire menu
    menu = parlour.get_menu()
    return parlour.get_menu()

@app.route('/menu/price', methods = ['GET'])
def get_item_price():
    # TODO
    req_data = request.get_json()
    item = json.loads(req_data)
    item_name = item['name']

    # menu = json.loads(parlour.get_menu())
    menu = parlour.menu_get()
    if (item_name in menu.pizzas):
        return str(menu.get_pizza_price(item_name))

    elif (item_name in menu.drinks):
        return str(menu.get_drink_price(item_name))

    elif (item_name in menu.toppings):
        return str(menu.get_topping_price(item_name))


@app.route('/menu/add_pizza', methods = ['POST'])
def add_pizza_type():
    req_data = request.get_json()
    custom_pizza = json.loads(req_data)

    pizza_name = custom_pizza['pizzaName']
    toppings = custom_pizza['toppings']

    results = parlour.add_pizza_to_menu(toppings, pizza_name)
    return results

if __name__ == "__main__":
    app.run(debug = True)
