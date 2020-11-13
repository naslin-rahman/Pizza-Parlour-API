from Classes.pizza import Pizza
from Classes.drinks import Drinks
from Classes.order import Order
from Classes.menu import Menu
from Classes.orderBuilder import OrderBuilder
import json
# TODO: Maybe put ordr builder in same file as order

class Parlour:
    def __init__(self):
        self.menu = Menu()
        self.orderNums = 0
        self.orders = {}
        self.orderBuilder = OrderBuilder()

    def check_valid_pizza(self, pizzaSize, pizzaType, pizzaToppings):
        for topping in pizzaToppings:
            if not (self.menu.check_valid_toppings(topping)):
                return -1

        return self.menu.check_valid_pizza(pizzaType) and self.menu.check_valid_sizes(pizzaSize)

    def check_valid_drink(self, drinkType):
        return self.menu.check_valid_drink(drinkType)

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

    def modify_pizza(self, pizzaSize, pizzaType, pizzaToppings, orderNum, pizzaNum, what_to_edit):
        # what_to_edit -> [1] Size    [2] Type    [3] Toppings
        orderToModify = self.orders[str(orderNum)]

        if (what_to_edit == "1"):
            if (self.menu.check_valid_sizes(pizzaSize)):
                orderToModify.change_size(pizzaSize, pizzaNum)
            else:
                return "Invalid Size"
        elif (what_to_edit == "2"):
            if (self.menu.check_valid_pizza(pizzaType)):
                orderToModify.change_type(pizzaType, pizzaNum)
            else:
                return "Invalid Pizza Type"
        else:
            toppings = pizzaToppings.split(',')

            for topping in toppings:
                if not (self.menu.check_valid_toppings(topping)):
                    return "Invalid Toppings"

            orderToModify.change_toppings(toppings, pizzaNum)


        self.orders[str(self.orderNums)] = orderToModify
        return "Changes succcefully made"

    def add_pizza(self, pizzaSize, pizzaType, pizzaToppings, orderNum):

        # Check valid pizza
        if not(self.check_valid_pizza(pizzaSize, pizzaType, pizzaToppings)):
            return "Invalid types"

        orderToModify = self.orders[str(orderNum)]
        pizza = self.orderBuilder.make_pizza(pizzaSize, pizzaType, pizzaToppings)
        orderToModify.add_pizza(pizza)
        self.orders[str(self.orderNums)] = orderToModify
        return "New pizza Successfully added"

    def delete_pizza(self, pizzaNum, orderNum):
        orderToModify = self.orders[str(orderNum)]
        success = orderToModify.remove_pizza(pizzaNum)

        if not (success):
            return "Pizza doesn't exist"

        self.orders[str(self.orderNums)] = orderToModify

        return "Pizza successfully removed"

    def modify_drink(self, drink_type, drink_num, order_num):
        # what_to_edit -> [1] Size    [2] Type    [3] Toppings
        orderToModify = self.orders[str(order_num)]

        if (self.menu.check_valid_drink(drink_type)):
            orderToModify.change_drink(drink_type, drink_num)
        else:
            return "Invalid drink type"

        self.orders[str(self.orderNums)] = orderToModify
        return "Changes succcefully made"

    def add_drink(self, drinkType, orderNum):
        if not(self.check_valid_drink(drinkType)):
            return "Invalid drink type"

        orderToModify = self.orders[str(self.orderNums)]
        drink = self.orderBuilder.make_drink(drinkType)
        orderToModify.add_drink(drink)
        self.orders[str(self.orderNums)] = orderToModify
        return "New drink successfully added"

    def delete_drink(self, drinkNum, orderNum):
        orderToModify = self.orders[str(orderNum)]
        success = orderToModify.remove_drink(drinkNum)

        if not (success):
            return "Drink doesn't exist"

        self.orders[str(self.orderNums)] = orderToModify

        return "Drink successfully removed"

    def cancel_order(self, order_num):
        if order_num in self.orders:
            del self.orders[str(order_num)]
            return "Order successfully removed"
        else:
            return "Order you're trying to remove does not exist"

    # Returns a specific order as a json string
    def get_order(self, order_num):
        if order_num in self.orders:

            orderToModify = self.orders[str(order_num)].get_order(self.menu);

            json_string = json.dumps(orderToModify, indent = 4, separators=(',',': '))
            return json_string
        else:
            return "Order does not exist"

    def get_menu(self):
        menu = self.menu.get_menu()
        json_string = json.dumps(menu, indent = 4, separators=(',',': '))
        return json_string

    def add_pizza_to_menu(self, toppingsStr, newPizza):
        toppings = toppingsStr.split(',')
        result = self.menu.add_pizza_type(newPizza, toppings)

        return result

    def menu_get(self):
        return self.menu
