from flask import Flask, request
from Classes.Parlour import Parlour
import json

app = Flask("Assignment 2")
parlour = Parlour()

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
    else:
        return "Not on menu"


@app.route('/menu/add_pizza_type', methods = ['POST'])
def add_pizza_type():
    req_data = request.get_json()
    custom_pizza = json.loads(req_data)

    pizza_name = custom_pizza['pizzaName']
    toppings = custom_pizza['toppings']

    results = parlour.add_pizza_to_menu(toppings, pizza_name)
    return results

@app.route('/new_order', methods = ['POST'])
def new_order():
    req_data = request.get_json()
    order_details = json.loads(req_data)

    num_pizzas = order_details['num_pizzas']
    num_drinks = order_details['num_drinks']
    size = order_details['size']
    type = order_details['type']
    toppings = order_details['toppings']
    drinks = order_details['drinks']

    results = parlour.new_order(num_pizzas, num_drinks, size, type, toppings, drinks)

    return results
### NEW
@app.route('/cancel_order', methods = ['POST'])
def cancel_order():
    req_data = request.get_json()
    order_details = json.loads(req_data)

    order_num = order_details['order_num']

    results = parlour.cancel_order(order_num)
    return results

@app.route('/show_order', methods = ['POST'])
def show_order():
    req_data = request.get_json()
    order_details = json.loads(req_data)

    order_num = order_details['order_num']

    results = parlour.get_order(order_num)
    return results

@app.route('/modify_order/add_pizza', methods = ['POST'])
def add_pizza():
    req_data = request.get_json()
    order_details = json.loads(req_data)

    pizza_size = order_details['new_size']
    pizza_type = order_details['new_type']
    pizza_toppings = order_details['new_toppings']
    order_to_edit = order_details['order_num']

    results = parlour.add_pizza(pizza_size, pizza_type, pizza_toppings, order_to_edit)
    return results

@app.route('/modify_order/remove_pizza', methods = ['POST'])
def remove_pizza():
    req_data = request.get_json()
    order_details = json.loads(req_data)

    pizza_num = order_details['pizza_num']
    order_to_edit = order_details['order_num']

    results = parlour.delete_pizza(pizza_num, order_to_edit)
    return results

@app.route('/modify_order/modify_pizza', methods = ['POST'])
def modify_pizza():
    req_data = request.get_json()
    order_details = json.loads(req_data)

    what_to_edit = order_details['what_to_edit']
    order_to_edit = order_details['order_num']
    num_pizza_to_update = order_details['pizza_num']
    new_size = order_details['new_size']
    new_type = order_details['new_type']
    new_toppings = order_details['new_toppings']

    results = parlour.modify_pizza(new_size, new_type, new_toppings, order_to_edit, num_pizza_to_update, what_to_edit)
    return results

@app.route('/modify_order/add_drink', methods = ['POST'])
def add_drink():
    req_data = request.get_json()
    order_details = json.loads(req_data)

    new_drink = order_details['new_drink']
    order_to_edit = order_details['order_num']

    results = parlour.add_drink(new_drink, order_to_edit)
    return results

@app.route('/modify_order/remove_drink', methods = ['POST'])
def remove_drink():
    req_data = request.get_json()
    order_details = json.loads(req_data)

    order_num = order_details['order_num']
    drink_num = order_details['drink_num']

    results = parlour.delete_drink(drink_num, order_num)
    return results

@app.route('/modify_order/modify_drink', methods = ['POST'])
def modify_drink():
    req_data = request.get_json()
    order_details = json.loads(req_data)

    order_to_edit = order_details['order_num']
    num_drink_to_update = order_details['drink_num']
    new_drink = order_details['new_drink']

    results = parlour.modify_drink(new_drink, num_drink_to_update, order_to_edit)
    return results

@app.route('/change_price', methods = ['POST'])
def change_price():
    req_data = request.get_json()
    order_details = json.loads(req_data)

    item = order_details['item']
    new_price = order_details['new_price']

    results = parlour.change_item_price(item, new_price)
    return results

@app.route('/deliver/uber', methods = ['POST'])
def deliver():
    req_data = request.get_json()
    order_info = json.loads(req_data)
    order = order_info['orderNum']
    address = order_info['address']

    details = parlour.get_order(order)
    return "Your delivery is on the way!"

@app.route('/deliver/foodora', methods = ['POST'])
def delivery():
    req_data = request.get_json()
    return "Your delivery is on the way!"

if __name__ == "__main__":
    app.run(debug = True)
