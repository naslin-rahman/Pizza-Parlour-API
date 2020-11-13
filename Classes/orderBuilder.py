from Classes.Pizza import Pizza
from Classes.Drinks import Drinks
from Classes.Order import Order

class OrderBuilder:
    def __init__(self):
        pass

    # Returns if valid size,type,toppings combo for a pizza
    def check_valid_pizza(self, pizza_size, pizza_type, pizza_toppings, menu):
        for topping in pizza_toppings:
            if not (menu.check_valid_toppings(topping)):
                return -1

        return menu.check_valid_pizza(pizza_type) and menu.check_valid_sizes(pizza_size)

    # Returns if drink type is valid
    def check_valid_drink(self, drink_type, menu):
        return menu.check_valid_drink(drink_type)

    # Return pizza object
    def make_pizza(self, size, type, toppings):
        pizza = Pizza(size, type, toppings)
        return pizza

    # Return drink object
    def make_drink(self, type):
        drink = Drinks(type)
        return drink

    # Returns an empty order that only contains the specific ordernum
    def make_order(self, ordernum):
        order = Order(ordernum)
        return order

    # Returns order object that contains all the needed pizzas and drinks
    def build_order(self, menu, num_pizzas, num_drinks, pizza_size, pizza_type, pizza_toppings, drink_type, orderNum):
        order = self.make_order(orderNum)

        for p in range(int(num_pizzas)):
            # TODO: add checking if valid
            toppings = pizza_toppings[p].split(',')

            if (self.check_valid_pizza(pizza_size[p], pizza_type[p], toppings, menu)):
                pizza = self.make_pizza(pizza_size[p], pizza_type[p], toppings)
                order.add_pizza(pizza)
            else:
                return -1

        for d in range(int(num_drinks)):
            if (self.check_valid_drink(drink_type[d], menu)):
                drink = self.make_drink(drink_type[d])
                order.add_drink(drink)
            else:
                return -1

        return order
