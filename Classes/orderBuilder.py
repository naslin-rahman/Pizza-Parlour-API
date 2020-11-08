from pizza.py import Pizza
from drinks.py import Drink
from order.py import Order

class OrderBuilder:
    def __init__(self):
        pass

    def makePizza(self, size, type, toppings):
        pizza = Pizza(size, type, toppings)
        return pizza

    def makeDrink(self, type):
        drink = Drink(type)
        return drink

    def makeOrder(self, ordernum):
        order = Order(ordernum)
        return order

    def buildOrder(self, pizzaSize, pizzaType, pizzaToppings, drinkType, orderNum):
        pizza = makePizza(pizzaSize, pizzaType, pizzaToppings)
        drink = makeDrink(drinkType)
        order = makeOrder(orderNum)
        order.addPizza(pizza)
        order.addDrink(drink)

        return order
