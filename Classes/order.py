from Classes.pizza.py import Pizza
from Classes.drinks.py import Drink

class Order:
  def __init__(self, ordernum):
    self.ordernum = ordernum
    self.cost = 0 # Default

    #Used for the creation of pizza in dictionary
    self.pizzaNum = 0
    self.drinkNum = 0

    #Used to count the pizzas and dirnks
    self.numPizzas = 0
    self.numDrinks = 0

    self.pizzas = {}
    self.drinks = {}

  def addPizza(self, pizza):
      self.pizzaNum += 1
      self.numPizzas += 1

      self.pizzas[str(self.pizzaNum)] = pizza

  def removePizza(self, pizzaNum):
      del self.pizzas[str(pizzaNum)]
      self.numPizzas -= 1

  def addDrink(self, drink):
      self.drinkNum += 1
      self.numDrinks += 1

      self.drinks[str(self.drinkNum)] = drink

  def removeDrink(self, drink):
      del self.drinks[str(drinkNum)]
      self.numDrinks -= 1

  def getCost(self, menu):
      cost = 0
      for pizza in self.pizzas.values():
          cost += pizza.getCost(menu)

      for drink in self.drinks.values():
          cost += drinks.getCost(menu)
