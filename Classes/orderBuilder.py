from Classes.pizza import Pizza
from Classes.drinks import Drinks
from Classes.order import Order

class OrderBuilder:
    def __init__(self):
        pass

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

            for topping in toppings:
                if not (menu.check_valid_toppings(topping)):
                    return -1

            if (menu.check_valid_pizza(pizzaType[p]) and menu.check_valid_sizes(pizzaSize[p])):
                pizza = self.make_pizza(pizzaSize[p], pizzaType[p], toppings)
                order.add_pizza(pizza)
            else:
                return -1

        for d in range(int(numDrinks)):
            if (menu.check_valid_drink(drinkType[d])):
                drink = self.make_drink(drinkType[d])
                order.add_drink(drink)
            else:
                return -1

        return order
