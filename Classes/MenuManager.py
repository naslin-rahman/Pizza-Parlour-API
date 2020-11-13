from Classes.Menu import Menu
import json

class MenuManager:
    def __init__(self):
        self.menu = Menu()

    # Returns the menu in a json file
    def get_menu(self):
        menu = self.menu.get_menu()
        json_string = json.dumps(menu, indent = 4, separators=(',',': '))
        return json_string

    # Adds a new type of pizza to the menu
    # toppings_str -> String representing the list of toppings
    # new_pizza    -> String representing the name of the new pizza
    # Note: Cost is default base 10 + cost of toppings
    def add_pizza_to_menu(self, toppings_str, new_pizza):
        toppings = toppings_str.split(',')
        result = self.menu.add_pizza_type(new_pizza, toppings)

        return result

    # Return reg menu object
    def menu_get(self):
        return self.menu
