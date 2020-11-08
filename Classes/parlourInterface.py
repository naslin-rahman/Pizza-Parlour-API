from pizza.py import Pizza
from drinks.py import Drink
from order.py import Order
from menu.py import Menu
from orderBuilder.py import OrderBuilder
import json
# TODO: Maybe put ordr builder in same file as order

class ParlourInterface:
    def __init__(self):
        self.menu = Menu()
        self.orderNums = 0
        self.orders = {}
        self.orderBuilder = OrderBuilder()

    def newOrder(self, pizzaSize, pizzaType, pizzaToppings, drinkType):
        # Assumes valid pizza size as string, valid pizza type as string
        # Assumes valid pizzaToppings as an array of strings
        # Assumes valid drinkType as strings
        # Default order is one pizza and one drink
        # TODO: Add empty cases - ex no dirnk just pizza
        # TODO: Add able to modify indiv orders
        self.orderNum += 1
        order = self.orderBuilder.buildOrder(pizzaSize, pizzaType, pizzaToppings, drinkType, self.orderNum)
        self.orders[str(self.ordernum)] = order

    def addPizza(self, pizzaSize, pizzaType, pizzaToppings, orderNum):
        orderToModify = self.orders[str(self.ordernum)]
        pizza = self.orderBuilder.makePizza(pizzaSize, pizzaType, pizzaToppings)
        orderToModify.addPizza(pizza)
        self.orders[str(self.ordernum)] = orderToModify

    def deletePizza(self, pizzaNum, orderNum):
        orderToModify = self.orders[str(self.ordernum)]
        orderToModify.removePizza(pizzaNum)
        self.orders[str(self.ordernum)] = orderToModify

    def addDrink(self, drinkType, orderNum):
        orderToModify = self.orders[str(self.ordernum)]
        drink = self.orderBuilder.makeDrink(drinkType)
        orderToModify.addDrink(drink)
        self.orders[str(self.ordernum)] = orderToModify

    def deleteDrink(self, drinkNum, orderNum):
        orderToModify = self.orders[str(self.ordernum)]
        orderToModify.removeDrink(drinkNum)
        self.orders[str(self.ordernum)] = orderToModify

    def addPizzaType(self, newType, toppingCombo, cost):
        # TODO add auto calc
        # Maybe 10 for base then add topping costs
        self.menu.pizzas[newType] = cost
        self.menu.pizzasPrep[newType] = toppingCombo

    def addDrinkType(self, newType, cost):
        self.menu.drinks[newType] = cost

    # Returns a specific order as a json string
    def getOrder(self, orderNum):
        orderToModify = self.orders[str(self.ordernum)]
        json_string = json.dumps(orderToModify)
        return json_string

    def getMenu(self):
        menu = self.menu.getMenu()
        json_string = json.dumps(menu)
        return json_string
