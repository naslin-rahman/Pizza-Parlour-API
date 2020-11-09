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

    def new_order(self, numPizzas, numDrinks, pizzaSize, pizzaType, pizzaToppings, drinkType):
        # Assumes valid pizza size as string, valid pizza type as string
        # Assumes valid pizzaToppings as an array of strings
        # Assumes valid drinkType as strings
        # Default order is one pizza and one drink
        # TODO: Add empty cases - ex no dirnk just pizza
        # TODO: Add able to modify indiv orders
        self.orderNums += 1
        order = self.orderBuilder.build_order(self.menu, numPizzas, numDrinks, pizzaSize, pizzaType, pizzaToppings, drinkType, self.orderNums)

        if (order == -1):
            return "Error: Invalid Type of Order Input"

        self.orders[str(self.orderNums)] = order
        cost = order.get_cost(self.menu)

        return "Order #" + str(self.orderNums) + " successfully added. Your order cost is: $" + str(cost)

    def add_pizza(self, pizzaSize, pizzaType, pizzaToppings, orderNum):
        orderToModify = self.orders[str(self.orderNums)]
        pizza = self.orderBuilder.make_pizza(pizzaSize, pizzaType, pizzaToppings)
        orderToModify.add_pizza(pizza)
        self.orders[str(self.orderNums)] = orderToModify

    def delete_pizza(self, pizzaNum, orderNum):
        orderToModify = self.orders[str(self.orderNums)]
        orderToModify.remove_pizza(pizzaNum)
        self.orders[str(self.orderNums)] = orderToModify

    def add_drink(self, drinkType, orderNum):
        orderToModify = self.orders[str(self.orderNums)]
        drink = self.orderBuilder.make_drink(drinkType)
        orderToModify.add_drink(drink)
        self.orders[str(self.orderNums)] = orderToModify

    def delete_drink(self, drinkNum, orderNum):
        orderToModify = self.orders[str(self.order/nums)]
        orderToModify.remove_drink(drinkNum)
        self.orders[str(self.orderNums)] = orderToModify

    # Returns a specific order as a json string
    def get_order(self, orderNum):
        orderToModify = self.orders[str(self.orderNums)]
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
