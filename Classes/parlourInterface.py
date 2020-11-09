from Classes.pizza import Pizza
from Classes.drinks import Drinks
from Classes.order import Order
from Classes.menu import Menu
from Classes.orderBuilder import OrderBuilder
import json
# TODO: Maybe put ordr builder in same file as order

class ParlourInterface:
    def __init__(self):
        self.menu = Menu()
        self.orderNums = 0
        self.orders = {}
        self.orderBuilder = OrderBuilder()

    def new_order(self, pizzaSize, pizzaType, pizzaToppings, drinkType):
        # Assumes valid pizza size as string, valid pizza type as string
        # Assumes valid pizzaToppings as an array of strings
        # Assumes valid drinkType as strings
        # Default order is one pizza and one drink
        # TODO: Add empty cases - ex no dirnk just pizza
        # TODO: Add able to modify indiv orders
        self.orderNum += 1
        order = self.orderBuilder.build_order(pizzaSize, pizzaType, pizzaToppings, drinkType, self.orderNum)
        self.orders[str(self.ordernum)] = order

    def add_pizza(self, pizzaSize, pizzaType, pizzaToppings, orderNum):
        orderToModify = self.orders[str(self.ordernum)]
        pizza = self.orderBuilder.make_pizza(pizzaSize, pizzaType, pizzaToppings)
        orderToModify.add_pizza(pizza)
        self.orders[str(self.ordernum)] = orderToModify

    def delete_pizza(self, pizzaNum, orderNum):
        orderToModify = self.orders[str(self.ordernum)]
        orderToModify.remove_pizza(pizzaNum)
        self.orders[str(self.ordernum)] = orderToModify

    def add_drink(self, drinkType, orderNum):
        orderToModify = self.orders[str(self.ordernum)]
        drink = self.orderBuilder.make_drink(drinkType)
        orderToModify.add_drink(drink)
        self.orders[str(self.ordernum)] = orderToModify

    def delete_drink(self, drinkNum, orderNum):
        orderToModify = self.orders[str(self.ordernum)]
        orderToModify.remove_drink(drinkNum)
        self.orders[str(self.ordernum)] = orderToModify

    # Returns a specific order as a json string
    def get_order(self, orderNum):
        orderToModify = self.orders[str(self.ordernum)]
        json_string = json.dumps(orderToModify)
        return json_string

    def get_menu(self):
        menu = self.menu.get_menu()
        json_string = json.dumps(menu)
        return json_string

    def add_pizza_to_menu(self, toppingsStr, newPizza):
        toppings = toppingsStr.split(',')
        result = self.menu.add_pizza_type(newPizza, toppings)

        return result

    def menu_get(self):
        return self.menu
