from Classes.Pizza import Pizza
from Classes.Drinks import Drinks
from Classes.Order import Order
from Classes.Menu import Menu
from Classes.OrderBuilder import OrderBuilder
import json
# TODO: Maybe put ordr builder in same file as order

class OrderManager:
    def __init__(self):
        self.order_nums = 0
        self.orders = {}
        self.order_builder = OrderBuilder()

    # Returns if the combination for the pizza is valid (on menu)
    def check_valid_pizza(self, pizza_size, pizza_type, pizza_toppings, menu):
        for topping in pizza_toppings:
            if not (menu.check_valid_toppings(topping)):
                return -1

        return menu.check_valid_pizza(pizza_type) and menu.check_valid_sizes(pizza_size)

    # Returns if the drink is valid (on menu)
    def check_valid_drink(self, drink_type, menu):
        return menu.check_valid_drink(drink_type)

    # Returns whether making a new order was successful based on parameters
    def new_order(self, num_pizzas, num_drinks, pizza_size, pizza_type, pizza_toppings, drink_type, menu):
        self.order_nums += 1
        order = self.order_builder.build_order(menu, num_pizzas, num_drinks, pizza_size, pizza_type, pizza_toppings, drink_type, self.order_nums)

        if (order == -1):
            return "Error: Invalid Type of Order Input"

        self.orders[str(self.order_nums)] = order
        cost = order.get_cost(menu)

        return "Order #" + str(self.order_nums) + " successfully added. Your order cost is: $" + str(cost)

    # Modify pizza specified by pizza_num in order #order_num
    # *** Only modifies if valid types
    # what_to_edit possible values: 1 -> Edit Size
    #                               2 -> Edit type
    #                               3 -> Edit toppings
    # Returns whether process was successful
    def modify_pizza(self, pizza_size, pizza_type, pizza_toppings, order_num, pizza_num, what_to_edit, menu):
        # what_to_edit -> [1] Size    [2] Type    [3] Toppings
        orderToModify = self.orders[str(order_num)]

        if (what_to_edit == "1"):
            if (menu.check_valid_sizes(pizza_size)):
                orderToModify.change_size(pizza_size, pizza_num)
            else:
                return "Invalid Size"
        elif (what_to_edit == "2"):
            if (menu.check_valid_pizza(pizza_type)):
                orderToModify.change_type(pizza_type, pizza_num)
            else:
                return "Invalid Pizza Type"
        else:
            toppings = pizza_toppings.split(',')

            for topping in toppings:
                if (not menu.check_valid_toppings(topping)):
                    return "Invalid Toppings"

            orderToModify.change_toppings(toppings, pizza_num)


        self.orders[str(self.order_nums)] = orderToModify
        return "Changes succcefully made"

    # Add a new pizza to order specified by order_num
    # Returns whether the process was successful
    def add_pizza(self, pizza_size, pizza_type, pizza_toppings, order_num, menu):

        # Check valid pizza
        if not(self.check_valid_pizza(pizza_size, pizza_type, pizza_toppings, menu)):
            return "Invalid types"

        orderToModify = self.orders[str(order_num)]
        pizza = self.order_builder.make_pizza(pizza_size, pizza_type, pizza_toppings)
        orderToModify.add_pizza(pizza)
        self.orders[str(self.order_nums)] = orderToModify
        return "New pizza Successfully added"

    # Deletes a specific pizza (pizza_num) from order specified by order_num
    # Returns whether the process was successful
    def delete_pizza(self, pizza_num, order_num):
        orderToModify = self.orders[str(order_num)]
        success = orderToModify.remove_pizza(pizza_num)

        if not (success):
            return "Pizza doesn't exist"

        self.orders[str(self.order_nums)] = orderToModify

        return "Pizza successfully removed"

    # Modify drink specified by drink_num in order #order_num
    # *** Only modifies if valid types
    # Returns whether process was successful
    def modify_drink(self, drink_type, drink_num, order_num, menu):
        # what_to_edit -> [1] Size    [2] Type    [3] Toppings
        orderToModify = self.orders[str(order_num)]

        if (menu.check_valid_drink(drink_type)):
            orderToModify.change_drink(drink_type, drink_num)
        else:
            return "Invalid drink type"

        self.orders[str(self.order_nums)] = orderToModify
        return "Changes succcefully made"

    # Add a new drink to order specified by order_num
    # Returns whether the process was successful
    def add_drink(self, drink_type, order_num, menu):
        if not(self.check_valid_drink(drink_type, menu)):
            return "Invalid drink type"

        orderToModify = self.orders[str(self.order_nums)]
        drink = self.order_builder.make_drink(drink_type)
        orderToModify.add_drink(drink)
        self.orders[str(self.order_nums)] = orderToModify
        return "New drink successfully added"

    # Deletes a specific drink (drink_num) from order specified by order_num
    # Returns whether the process was successful
    def delete_drink(self, drink_num, order_num):
        orderToModify = self.orders[str(order_num)]
        success = orderToModify.remove_drink(drink_num)

        if not (success):
            return "Drink doesn't exist"

        self.orders[str(self.order_nums)] = orderToModify

        return "Drink successfully removed"

    # Cancel order (order_num) by removing it from order manager
    # Returns if process was successful
    def cancel_order(self, order_num):
        if order_num in self.orders:
            del self.orders[str(order_num)]
            return "Order successfully removed"
        else:
            return "Order you're trying to remove does not exist"

    # Returns a specific order as a json string
    def get_order(self, order_num, menu):
        if order_num in self.orders:

            orderToModify = self.orders[str(order_num)].get_order(menu)

            json_string = json.dumps(orderToModify, indent = 4, separators=(',',': '))
            return json_string
        else:
            return "Order does not exist"
