from Classes.pizza import Pizza
from Classes.drinks import Drinks

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

  def add_pizza(self, pizza):
      self.pizzaNum += 1
      self.numPizzas += 1

      self.pizzas[str(self.pizzaNum)] = pizza

  def remove_pizza(self, pizzaNum):
      del self.pizzas[str(pizzaNum)]
      self.numPizzas -= 1

  def add_drink(self, drink):
      self.drinkNum += 1
      self.numDrinks += 1

      self.drinks[str(self.drinkNum)] = drink

  def remove_drink(self, drink):
      del self.drinks[str(drinkNum)]
      self.numDrinks -= 1

  def get_cost(self, menu):
      cost = 0
      for pizza in self.pizzas.values():
          cost += pizza.get_cost(menu)

      for drink in self.drinks.values():
          cost += drinks.get_cost(menu)
