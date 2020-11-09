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
      if pizzaNum in self.pizzas:
          del self.pizzas[str(pizzaNum)]
          self.numPizzas -= 1
          return "Pizza successfully removed"
      else:
          return "Pizza you're trying to remove does not exist"

  def change_size(self, size, pizzaNum):
      self.pizzas[str(pizzaNum)].change_size(size)

  def change_type(self, type, pizzaNum):
      self.pizzas[str(pizzaNum)].change_type(type)

  def change_toppings(self, toppings, pizzaNum):
      self.pizzas[str(pizzaNum)].change_toppings(toppings)

  def add_drink(self, drink):
      self.drinkNum += 1
      self.numDrinks += 1

      self.drinks[str(self.drinkNum)] = drink

  def remove_drink(self, drinkNum):
      if drinkNum in self.drinks:
          del self.drinks[str(drinkNum)]
          self.numDrinks -= 1
          return "Drink successfully removed"
      else:
          return "Drink you're trying to remove does not exist"

  def change_drink(self, drink_type, drink_num):
      self.drinks[str(drink_num)].change_type(drink_type)

  def get_cost(self, menu):
      cost = 0
      for pizza in self.pizzas.values():
          cost += pizza.get_cost(menu)

      for drink in self.drinks.values():
          cost += drink.get_cost(menu)

      return cost
