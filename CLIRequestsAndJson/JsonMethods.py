import json

# Methods for converting user input into json text that can be passed onto the flask app
def add_custom_json(toppings, pizza_name):
    dict = {}
    dict["toppings"] = toppings
    dict["pizzaName"] = pizza_name
    return json.dumps(dict)

def show_order_json(order_num):
    dict = {}
    dict["order_num"] = order_num
    json_string = json.dumps(dict)
    return json_string

def cancel_order_json(order_num):
    dict = {}
    dict["order_num"] = order_num

    return json.dumps(dict)

def show_menu_item_json(item):
    dict = {}
    dict["name"] = item

    return json.dumps(dict)

def order_pizzas_drinks_json(num_pizzas, num_drinks, size, type, toppings, drinks):
    dict = {}
    dict['num_pizzas'] = num_pizzas
    dict['num_drinks'] = num_drinks
    dict['size'] = size
    dict['type'] = type
    dict['toppings'] = toppings
    dict['drinks'] = drinks
    return json.dumps(dict)

def modify_pizza_json(what_to_edit, order_to_edit, num_pizza_to_update, new_size, new_type, new_toppings):
    dict = {}
    dict['what_to_edit'] = what_to_edit
    dict['order_num'] = order_to_edit
    dict['pizza_num'] = num_pizza_to_update
    dict['new_size'] = new_size
    dict['new_type'] = new_type
    dict['new_toppings'] = new_toppings
    return json.dumps(dict)

def add_one_pizza_json(order_to_edit, size, type, toppings):
    dict = {}
    dict['order_num'] = order_to_edit
    dict['new_size'] = size
    dict['new_type'] = type
    dict['new_toppings'] = toppings
    return json.dumps(dict)

def delete_pizza_json(order_to_edit, pizza_num):
    dict = {}
    dict['order_num'] = order_to_edit
    dict['pizza_num'] = pizza_num
    return json.dumps(dict)

def modify_drink_json(order_to_edit, num_drink_to_update, new_drink):
    dict = {}
    dict['order_num'] = order_to_edit
    dict['drink_num'] = num_drink_to_update
    dict['new_drink'] = new_drink
    return json.dumps(dict)

def add_one_drink_json(order_to_edit, new_drink):
    dict = {}
    dict['order_num'] = order_to_edit
    dict['new_drink'] = new_drink
    return json.dumps(dict)

def remove_drink_json(order_to_edit, drink_num):
    dict = {}
    dict['order_num'] = order_to_edit
    dict['drink_num'] = drink_num
    return json.dumps(dict)

def change_price_json(item, new_price):
    dict = {}
    dict['item'] = item
    dict['new_price'] = new_price
    return json.dumps(dict)

def delivery_UE_json(order_num, address):
    dict = {}
    dict["orderNum"] = int(order_num)
    dict["address"] = address

    return json.dumps(dict)

def delivery_F_json(order_num, address):
    new_str = order_num + ',' + address
    dict = {}
    dict["csv details"] = new_str
    return json.dumps(dict)
