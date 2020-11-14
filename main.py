import os
from CLIRequestsAndJson.RequestMethods import *

# Returns if a number is an valid input
def valid_num_input(input):
    if input != "":
        try:
            int(input)

            if int(input) >= 0:
                return True
            else:
                return "Negative numbers are not allowed"
        except ValueError:
            return "Please enter an integer"
    return "Please enter a non-empty integer"

# Add a new pizza with a custom toppings/prep combo
def add_custom():
    toppings = input("What toppings would you like on your new custom pizza?\n")
    pizzaName = input("What would you like to call your custom pizza?\n")

    result = add_custom_get(toppings, pizzaName)

    print(result.text)

# Show an order
def show_order():
    order_num = input("What is the number of the order you'd like to see?\n")
    check = valid_num_input(order_num)

    if (check is not True):
        print(check)
    else:
        r = show_order_post(order_num)

        print(r.text)

# Cancels an order
def cancel_order():
    order_num = input("What is the number of the order you'd like to cancel?\n")
    check = valid_num_input(order_num)

    if (check is not True):
        print(check)
    else:
        r = cancel_order_post(order_num)
        print(r.text)

# Shows the price of a specific item
def show_menu_item_get(item):
    json_string = show_menu_item_get(item)
    return requests.get('http://127.0.0.1:5000/menu/price', json=json_string)

# Shows eveyrhting on the menu + cost
def show_menu():
    view_menu = input("Would you like to view the entire menu?\n[1] Yes     [2] No\n")
    if (view_menu == "1"):
        os.system('curl http://127.0.0.1:5000/menu')

    elif (view_menu == "2"):
        item = input("Please enter item name to see cost\n")

        r = show_menu_item_get(item)

        print("$" + r.text)
    else:
        print ("Not a valid option")

# Make a new order
def order_pizzas_drinks():
    #Enter number of pizzas and drinks
    countedPizzas = 0
    countedDrinks = 0
    numPizzas = input("How many pizzas would you like?\n")
    check = valid_num_input(numPizzas)

    if (check is not True):
        print(check)
    else:
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
                print("Invalid option\n")
                invalid = True
                break;
            type[countedPizzas] = input("Enter valid pizza type: \n")
            toppings[countedPizzas] = input("Enter extra toppings (seperated by a single comma): ")
            countedPizzas += 1

        if invalid is not True:
            numDrinks = input("How many drinks would you like?\n")
            check = valid_num_input(numDrinks)

            if (check is not True):
                print(check)
            else:
                drinks = [''] * int(numDrinks)

                while (countedDrinks != int(numDrinks)):
                    #Enter pizza vals
                    drinks[countedDrinks] = input(f"Enter drink name for Drink #{countedDrinks + 1} \n")
                    countedDrinks += 1

                result = order_pizzas_drinks_post(numPizzas, numDrinks, size, type, toppings, drinks)

                print(result.text)

# Updates a pizza in an order
# Types of edit values: 1 -> Add new pizza
#                       2 -> Delete pizza
#                       3 -> Modify a pizza
def update_pizzas(order_to_edit, types_of_edit):
    if (types_of_edit == "3"):
        num_pizza_to_update = input("Enter the pizza number you want to edit\n")
        check = valid_num_input(num_pizza_to_update)

        if (check is not True):
            print(check)
        else:
            what_to_edit = input("What would you like to edit?\n[1] Size    [2] Type    [3] Toppings\n")

            cont = True
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
                cont = False
                print("Not a valid option\n")

            if cont:
                result = modify_pizza_post(what_to_edit, order_to_edit, num_pizza_to_update, new_size, new_type, new_toppings)

                print(result.text)

    elif (types_of_edit == "1"):
        size = input("Enter pizza size (Small, Medium, Large): \n")
        type = input("Enter valid pizza type: \n")
        toppings = input("Enter extra toppings (seperated by a single comma): \n")

        result = add_one_pizza_post(order_to_edit, size, type, toppings)

        print(result.text)

    elif (types_of_edit == "2"):
        pizza_num = input("Enter the pizza num you'd like to remove\n")
        check = valid_num_input(pizza_num)

        if (check is not True):
            print(check)
        else:
            result = delete_pizza_post(order_to_edit, pizza_num)

            print(result.text)

# Updates a drink in an order
# Types of edit values: 1 -> Add new drink
#                       2 -> Delete drink
#                       3 -> Modify a drink
def update_drinks(order_to_edit, types_of_edit):
    if (types_of_edit == "3"):
        num_drink_to_update = input("Enter the drink number you want to edit\n")
        check = valid_num_input(num_drink_to_update)

        if (check is not True):
            print(check)
        else:
            new_drink = input("New drink type? \n")
            result = modify_drink_post(order_to_edit, num_drink_to_update, new_drink)
            print(result.text)

    elif (types_of_edit == "1"):
        new_drink = input("New drink type? \n")
        result = add_drink_post(order_to_edit, new_drink)
        print(result.text)

    elif (types_of_edit == "2"):
        drink_num = input("Enter the drink num you'd like to remove\n")
        check = valid_num_input(drink_num)

        if (check is not True):
            print(check)
        else:
            result = remove_drink_post(order_to_edit, drink_num)
            print(result.text)

# Updates an order
def update_order():
    while(True):
        update_pizza = input("Would you like to update an order?\n[1] Yes   [2] No\n")
        if (update_pizza == "1"):
            order_to_edit = input("Enter the order number you want to edit:\n")
            pizza_or_drink = input("What would you like to edit?\n[1] Pizza     [2] Drink\n")

            if (pizza_or_drink == "1"):
                types_of_edit = input("What changes would you like to make?\n[1] Add pizzas     [2] Remove pizza    [3] Edit pizza\n")
                update_pizzas(order_to_edit, types_of_edit )

            elif (pizza_or_drink == "2"):
                types_of_edit = input("What changes would you like to make?\n[1] Add drinks     [2] Remove drink    [3] Edit drink\n")
                update_drinks(order_to_edit, types_of_edit)

            else:
                print("Not a valid option\n")

        else:
            pass

        done = input("Are you done ordering?\n [1] Yes   [2] No\n")
        if (done == "1"):
            break

# Change the price of somthing on the menu
def change_price():
    item = input("Please enter item name who's price you want to change\n")
    r = show_menu_item_get(item)
    new_price = input("The current price is $" + r.text + ". What is the new price?\n")
    check = valid_num_input(new_price)

    if (check is not True):
        print(check)
    else:
        result = change_price_post(item, new_price)
        print(result.text)

# Deliver an order
def delivery(delivery_type):
    if (delivery_type == "Pickup"):
        print("Your order is on its way!")

    else:
        order_num = input("Enter your order #: \n")
        address = input("Enter your address:\n")
        if (delivery_type == "Uber Eats"):
            result = delivery_UE_request(order_num, address)
            print(result.text)

        elif (delivery_type == "Foodora"):
            result = delivery_F_request(order_num, address)
            print(result.text)

# Main client interface
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

        if (action == "change price"):
            change_price()

    # Ask user what delivery method they want
    delivery_type = input("Enter your method of delivery:\n")
    delivery(delivery_type)

if __name__ == "__main__":
    os.system('curl http://127.0.0.1:5000/pizza')
    print("\n")
    cli()
