import os
import json
import requests

def add_custom():
    toppings = input("What toppings would you like on your new custom pizza?\n")
    pizzaName = input("What would you like to call your custom pizza?\n")

    dict = {}
    dict["toppings"] = toppings
    dict["pizzaName"] = pizzaName

    json_string = json.dumps(dict)

    result = requests.post('http://127.0.0.1:5000/menu/add_pizza_type', json=json_string)

    print(result.text)

def show_order():
    order_num = input("What is the number of the order you'd like to see?\n")
    dict = {}
    dict["order_num"] = order_num

    json_string = json.dumps(dict)

    r = requests.post('http://127.0.0.1:5000/show_order', json=json_string)

    print(r.text)

def cancel_order():
    order_num = input("What is the number of the order you'd like to cancel?\n")
    dict = {}
    dict["order_num"] = order_num

    json_string = json.dumps(dict)

    r = requests.post('http://127.0.0.1:5000/cancel_order', json=json_string)

    print(r.text)

def show_menu():
    view_menu = input("Would you like to view the entire menu?\n")
    if (view_menu == "yes"):
        os.system('curl http://127.0.0.1:5000/menu') # A get request i think?

    elif (view_menu == "no"):
        item = input("Please enter item name to see cost\n")

        dict = {}
        dict["name"] = item

        json_string = json.dumps(dict)

        r = requests.get('http://127.0.0.1:5000/menu/price', json=json_string)

        print("$" + r.text)

def order_pizzas_drinks():
    #Enter number of pizzas and drinks
    countedPizzas = 0
    countedDrinks = 0
    numPizzas = input("How many pizzas would you like?\n")
    size = ['Small'] * int(numPizzas)
    type = [''] * int(numPizzas)
    toppings = [''] * int(numPizzas)
    invalid = False
    while (countedPizzas != int(numPizzas) and not invalid):
        #Enter pizza vals
        size[countedPizzas] = input(f"Pizza #{countedPizzas + 1} \nWhat pizza size?\n[1] Small      [2] Medium      [3] Large \n")
        if (size[countedPizzas] == '1'):
            size[countedPizzas] = 'Small'
        elif (size[countedPizzas] == '2'):
            size[countedPizzas] = 'Medium'
        elif (size[countedPizzas] == '3'):
            size[countedPizzas] = 'Large'
        else:
            print("Invalid size\n")
            invalid = True
            break;
        type[countedPizzas] = input("Enter valid pizza type: \n")
        toppings[countedPizzas] = input("Enter extra toppings (seperated by a single comma): ")
        countedPizzas += 1

    if invalid is not True:
        numDrinks = input("How many drinks would you like?\n")
        drinks = [''] * int(numDrinks)


        while (countedDrinks != int(numDrinks)):
            #Enter pizza vals
            drinks[countedDrinks] = input(f"Enter drink name for Drink #{countedDrinks + 1} \n")
            countedDrinks += 1

        dict = {}
        dict['numPizzas'] = numPizzas
        dict['numDrinks'] = numDrinks
        dict['size'] = size
        dict['type'] = type
        dict['toppings'] = toppings
        dict['drinks'] = drinks
        json_string = json.dumps(dict)

        result = requests.post('http://127.0.0.1:5000/new_order', json=json_string)

        print(result.text)

def update_pizzas(types_of_edit):
    if (types_of_edit == "3"):
        num_pizza_to_update = input("Enter the pizza number you want to edit\n")
        what_to_edit = input("What would you like to edit?\n[1] Size    [2] Type    [3] Toppings\n")

        new_size = ""
        new_type = ""
        new_toppings = ""

        if (what_to_edit == "1"):
            new_size = input("New size of pizza? (Small, Medium, Large)\n")

        elif(what_to_edit == "2"):
            new_type = input("New pizza type?\n")

        elif(what_to_edit == "3"):
            new_toppings = input("New toppings combo? \n")

        else:
            print("Not a valid option\n")

        dict = {}
        dict['what_to_edit'] = what_to_edit
        dict['order_num'] = order_to_edit
        dict['pizza_num'] = num_pizza_to_update
        dict['new_size'] = new_size
        dict['new_type'] = new_type
        dict['new_toppings'] = new_toppings
        json_string = json.dumps(dict)

        result = requests.post('http://127.0.0.1:5000/modify_order/modify_pizza', json=json_string)

        print(result.text)

        # TODO add link and print results
    elif (types_of_edit == "1"):
        size = input("Enter pizza size (Small, Medium, Large): \n")
        type = input("Enter valid pizza type: \n")
        toppings = input("Enter extra toppings (seperated by a single comma): \n")

        dict = {}
        dict['order_num'] = order_to_edit
        dict['new_size'] = size
        dict['new_type'] = type
        dict['new_toppings'] = toppings
        json_string = json.dumps(dict)

        result = requests.post('http://127.0.0.1:5000/modify_order/add_pizza', json=json_string)

        print(result.text)

    elif (types_of_edit == "2"):
        pizza_num = input("Enter the pizza num you'd like to remove\n")

        dict = {}
        dict['order_num'] = order_to_edit
        dict['pizza_num'] = pizza_num
        json_string = json.dumps(dict)

        result = requests.post('http://127.0.0.1:5000/modify_order/remove_pizza', json=json_string)

        print(result.text)

def update_drinks(types_of_edit):
    if (types_of_edit == "3"):
        num_drink_to_update = input("Enter the drink number you want to edit\n")
        new_drink = input("New drink type? \n")

        dict = {}
        dict['order_num'] = order_to_edit
        dict['drink_num'] = num_drink_to_update
        dict['new_drink'] = new_drink
        json_string = json.dumps(dict)

        result = requests.post('http://127.0.0.1:5000/modify_order/modify_drink', json=json_string)

        print(result.text)

        # TODO add link and print results
    elif (types_of_edit == "1"):
        new_drink = input("New drink type? \n")

        dict = {}
        dict['order_num'] = order_to_edit
        dict['new_drink'] = new_drink
        json_string = json.dumps(dict)

        result = requests.post('http://127.0.0.1:5000/modify_order/add_drink', json=json_string)

        print(result.text)

    elif (types_of_edit == "2"):
        drink_num = input("Enter the drink num you'd like to remove\n")

        dict = {}
        dict['order_num'] = order_to_edit
        dict['drink_num'] = drink_num
        json_string = json.dumps(dict)

        result = requests.post('http://127.0.0.1:5000/modify_order/remove_drink', json=json_string)

        print(result.text)

def update_order():
    while(True):
        update_pizza = input("Would you like to update an order?\n[1] Yes   [2] No\n")
        if (update_pizza == "1"):
            order_to_edit = input("Enter the order number you want to edit:\n")
            pizza_or_drink = input("What would you like to edit?\n[1] Pizza     [2] Drink\n")

            if (pizza_or_drink == "1"):
                types_of_edit = input("What changes would you like to make?\n[1] Add pizzas     [2] Remove pizza    [3] Edit pizza\n")
                update_pizzas(types_of_edit)

            elif (pizza_or_drink == "2"):
                types_of_edit = input("What changes would you like to make?\n[1] Add drinks     [2] Remove drink    [3] Edit drink\n")
                update_drinks(types_of_edit)

            else:
                print("Not a valid option\n")

        else:
            pass

        done = input("Are you done ordering?\n [1] Yes   [2] No\n")
        if (done == "1"):
            break

def delivery(delivery_type):
    if (delivery_type == "Pickup"):
        print("Your order is on its way!")

    else:
        order_num = input("Enter your order #: \n")
        address = input("Enter your address:\n")
        if (delivery_type == "Uber Eats"):
            dict = {}
            dict["orderNum"] = int(order_num)
            dict["address"] = address

            json_string = json.dumps(dict)

            result = requests.post('http://127.0.0.1:5000/deliver/uber', json=json_string)
            print(result.text)

        elif (delivery_type == "Foodora"):
            new_str = order_num + ',' + address
            dict = {}
            dict["csv details"] = new_str
            json_string = json.dumps(dict)

            result = requests.post('http://127.0.0.1:5000/deliver/foodora', json=json_string)
            print(result.text)

def cli():
    ordering = True

    while(ordering):
        action = input("What would you like to do?:\n") #order, menu, item price update, cancel
        #print("yeet\n")
        if (action == "quit"):
            ordering = False

        if (action == "show order"):
            show_order()

        if (action == "cancel order"):
            cancel_order()

        if (action == "menu"):
            show_menu()

        if (action == "custom"):
            add_custom()

        if (action == "order"):
            order_pizzas_drinks()

        if (action == "update"):
            update_order()

    # Ask user what delivery method they want
    delivery_type = input("Enter your method of delivery:\n")
    delivery(delivery_type)

if __name__ == "__main__":
    os.system('curl http://127.0.0.1:5000/pizza')
    print("\n")
    cli()
