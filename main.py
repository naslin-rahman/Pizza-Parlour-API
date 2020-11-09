import os
import json
import requests

def cli():
    action = input("What would you like to do?:\n") #order, menu, item price update, cancel
    #print("yeet\n")
    if (action == "menu"):
        # TODO enter item and get back price

        view_menu = input("Would you like to view the entire menu?\n")
        if (view_menu == "yes"):
            os.system('curl http://127.0.0.1:5000/menu') # A get request i think?

        elif (view_menu == "no"):
            item = input("Please enter item name to see cost\n")

    if (action == "add custom pizza"):
        toppings = input("What toppings would you like on your new custom pizza?")
        pizzaName = input("What would you like to call your custom pizza?")

        dict = {}
        dict["toppings"] = toppings
        dict["pizzaName"] = pizzaName

        json_string = json.dumps(dict)

        result = requests.post('http://127.0.0.1:5000/menu/add_pizza', json=json_string)

        print(result.text)


    if (action == "order"):
        #Enter number of pizzas and drinks
        countedPizzas = 0
        countedDrinks = 0
        numPizzas = input("How many pizzas would you like?\n")

        while (countedPizzas != int(numPizzas)):
            #Enter pizza vals
            pizzaOrder = input(f"Enter pizza order (size, type, toppings) for Pizza #{countedPizzas + 1} \n")
            countedPizzas += 1

        numDrinks = input("How many drinks would you like?\n")
        while (countedDrinks != int(numDrinks)):
            #Enter pizza vals
            drinkOrder = input(f"Enter drink name for Drink #{countedDrinks + 1} \n")
            countedDrinks += 1

    if (action == "update"):
        while(True):
            update_pizza = input("Would you like to update a pizza?\n")
            if (update_pizza == "yes"):
                num_pizza_to_update = input("Enter the pizza #\n")
                new_pizza_order = input(f"Enter pizza order (size, type, toppings) for Pizza #{int(num_pizza_to_update)} \n")
            else:
                pass

            done = input("Are you done?\n")
            if (done == "yes"):
                break

if __name__ == "__main__":
    os.system('curl http://127.0.0.1:5000/pizza')
    print("\n")
    cli()
