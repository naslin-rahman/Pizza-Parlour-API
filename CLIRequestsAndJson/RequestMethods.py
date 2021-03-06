from CLIRequestsAndJson.JsonMethods import *
import requests

# Methods for sending requests to the flask app
def add_custom_post(toppings, pizza_name):
    json_string = add_custom_json(toppings, pizza_name)
    return requests.post('http://127.0.0.1:5000/menu/add_pizza_type', json=json_string)

def show_order_post(order_num):
    json_string = show_order_json(order_num)
    return requests.post('http://127.0.0.1:5000/show_order', json=json_string)

def cancel_order_post(order_num):
    json_string = cancel_order_json(order_num)
    return requests.post('http://127.0.0.1:5000/cancel_order', json=json_string)

# Shows the price of a specific item
def show_menu_item_get(item):
    json_string = show_menu_item_json(item)
    return requests.get('http://127.0.0.1:5000/menu/price', json=json_string)

def order_pizzas_drinks_post(num_pizzas, num_drinks, size, type, toppings, drinks):
    json_string = order_pizzas_drinks_json(num_pizzas, num_drinks, size, type, toppings, drinks)
    return requests.post('http://127.0.0.1:5000/new_order', json=json_string)

def modify_pizza_post(what_to_edit, order_to_edit, num_pizza_to_update, new_size, new_type, new_toppings):
    json_string = modify_pizza_json(what_to_edit, order_to_edit, num_pizza_to_update, new_size, new_type, new_toppings)
    return requests.post('http://127.0.0.1:5000/modify_order/modify_pizza', json=json_string)

def add_one_pizza_post(order_to_edit, size, type, toppings):
    json_string = add_one_pizza_json(order_to_edit, size, type, toppings)
    return requests.post('http://127.0.0.1:5000/modify_order/add_pizza', json=json_string)

def delete_pizza_post(order_to_edit, pizza_num):
    json_string = delete_pizza_json(order_to_edit, pizza_num)
    return requests.post('http://127.0.0.1:5000/modify_order/remove_pizza', json=json_string)

def modify_drink_post(order_to_edit, num_drink_to_update, new_drink):
    json_string = modify_drink_json(order_to_edit, num_drink_to_update, new_drink)
    return requests.post('http://127.0.0.1:5000/modify_order/modify_drink', json=json_string)

def add_one_drink_post(order_to_edit, new_drink):
    json_string = add_one_drink_json(order_to_edit, new_drink)
    return requests.post('http://127.0.0.1:5000/modify_order/add_drink', json=json_string)

def remove_drink_post(order_to_edit, drink_num):
    json_string = remove_drink_json(order_to_edit, drink_num)
    return requests.post('http://127.0.0.1:5000/modify_order/remove_drink', json=json_string)

def change_price_post(item, new_price):
    json_string = change_price_json(item, new_price)
    return requests.post('http://127.0.0.1:5000/change_price', json=json_string)

def delivery_UE_request(order_num, address):
    json_string = delivery_UE_json(order_num, address)
    return requests.post('http://127.0.0.1:5000/deliver/uber', json=json_string)

def delivery_F_request(order_num, address):
    json_string = delivery_F_json(order_num, address)
    return requests.post('http://127.0.0.1:5000/deliver/foodora', json=json_string)
