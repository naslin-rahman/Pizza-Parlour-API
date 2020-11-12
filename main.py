import os
import json
import requests

def cli():
    ordering = True

    while(ordering):
        action = input("What would you like to do?:\n") #order, menu, item price update, cancel
        #print("yeet\n")
        if (action == "quit"):
            ordering = False

        if (action == "menu"):
            # TODO enter item and get back price

            view_menu = input("Would you like to view the entire menu?\n")
            if (view_menu == "yes"):
                os.system('curl http://127.0.0.1:5000/menu') # A get request i think?

            elif (view_menu == "no"):
                item = input("Please enter item name to see cost\n")

                dict = {}
                dict["name"] = item

                json_string = json.dumps(dict)

                r = requests.get('http://127.0.0.1:5000/menu/price', json=json_string)

                print(r.text)

        if (action == "add custom pizza"):
            toppings = input("What toppings would you like on your new custom pizza?\n")
            pizzaName = input("What would you like to call your custom pizza?\n")

            dict = {}
            dict["toppings"] = toppings
            dict["pizzaName"] = pizzaName

            json_string = json.dumps(dict)

            result = requests.post('http://127.0.0.1:5000/menu/add_pizza_type', json=json_string)

            print(result.text)


        if (action == "order"):
            #Enter number of pizzas and drinks
            countedPizzas = 0
            countedDrinks = 0
            numPizzas = input("How many pizzas would you like?\n")
            size = ['Small'] * int(numPizzas)
            type = [''] * int(numPizzas)
            toppings = [''] * int(numPizzas)

            while (countedPizzas != int(numPizzas)):
                #Enter pizza vals
                size[countedPizzas] = input(f"Pizza #{countedPizzas + 1} \nEnter pizza size (Small, Medium, Large): \n")
                type[countedPizzas] = input("Enter valid pizza type: \n")
                toppings[countedPizzas] = input("Enter extra toppings (seperated by a single comma): ")
                countedPizzas += 1

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

        if (action == "update"):
            while(True):
                update_pizza = input("Would you like to update an order?\n[1] Yes   [2] No\n")
                if (update_pizza == "1"):
                    order_to_edit = input("Enter the order number you want to edit:\n")
                    pizza_or_drink = input("What would you like to edit?\n[1] Pizza     [2] Drink\n")

                    if (pizza_or_drink == "1"):
                        types_of_edit = input("What changes would you like to make?\n[1] Add pizzas     [2] Remove pizza    [3] Edit pizza\n")

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


                    elif (pizza_or_drink == "2"):
                        types_of_edit = input("What changes would you like to make?\n[1] Add drinks     [2] Remove drink    [3] Edit drink\n")

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

                    else:
                        print("Not a valid option\n")

                else:
                    pass

                done = input("Are you done ordering?\n [1] Yes   [2] No\n")
                if (done == "1"):
                    break
        
    # Ask user what delivery method they want
    deliveryType = input("Enter your method of delivery:\n")
    if (deliveryType == "Uber eats"):
        order_num = input("Enter your order: #\n")
        address = input("Enter your address:\n")

        dict = {}
        dict["orderNum"] = int(order_num)
        dict["address"] = address

        json_string = json.dumps(dict)

        result = requests.post('http://127.0.0.1:5000/deliver', json=json_string)
        print(result.text)
    
    elif (deliveryType == "Pickup"):
        print("Your order is on its way!")

if __name__ == "__main__":
    os.system('curl http://127.0.0.1:5000/pizza')
    print("\n")
    cli()
