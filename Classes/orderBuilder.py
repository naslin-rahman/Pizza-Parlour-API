from Classes.pizza import Pizza
from Classes.drinks import Drinks
from Classes.order import Order

class OrderBuilder:
    def __init__(self):
        pass

    def check_valid_pizza(self, pizzaSize, pizzaType, pizzaToppings, menu):
        for topping in pizzaToppings:
            if not (menu.check_valid_toppings(topping)):
                return -1

        return menu.check_valid_pizza(pizzaType) and menu.check_valid_sizes(pizzaSize)

    def check_valid_drink(self, drinkType, menu):
        return menu.check_valid_drink(drinkType)

    def make_pizza(self, size, type, toppings):
        pizza = Pizza(size, type, toppings)
        return pizza

    def make_drink(self, type):
        drink = Drinks(type)
        return drink

    def make_order(self, ordernum):
        order = Order(ordernum)
        return order

    def build_order(self, menu, numPizzas, numDrinks, pizzaSize, pizzaType, pizzaToppings, drinkType, orderNum):
        order = self.make_order(orderNum)

        for p in range(int(numPizzas)):
            # TODO: add checking if valid
            toppings = pizzaToppings[p].split(',')

            if (self.check_valid_pizza(pizzaSize[p], pizzaType[p], toppings, menu)):
                pizza = self.make_pizza(pizzaSize[p], pizzaType[p], toppings)
                order.add_pizza(pizza)
            else:
                return -1

        for d in range(int(numDrinks)):
            if (self.check_valid_drink(drinkType[d], menu)):
                drink = self.make_drink(drinkType[d])
                order.add_drink(drink)
            else:
                return -1

        return order
