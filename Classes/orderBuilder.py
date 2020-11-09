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
        drink = Drink(type)
        return drink

    def make_order(self, ordernum):
        order = Order(ordernum)
        return order

    def build_order(self, pizzaSize, pizzaType, pizzaToppings, drinkType, orderNum):
        pizza = make_pizza(pizzaSize, pizzaType, pizzaToppings)
        drink = make_drink(drinkType)
        order = make_order(orderNum)
        order.add_pizza(pizza)
        order.add_drink(drink)

        return order
