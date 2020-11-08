from Classes.menu.py import Menu

class Pizza:
  def __init__(self, size, type, toppings):
    self.size = size
    self.type = type
    self.toppings = toppings

    self.cost = getCost(self)

  def makePizza(self):
      return self

  def getCost(self, menu):
      cost = 0
      # Switch based on type + toppings + size for cost
      baseCost = menu.pizzas.get(self.type)
      toppingCost = 0
      for topping in self.toppings:
          toppingCost += menu.toppings.get(topping)

      return baseCost + toppingCost

  # Might bot
  def addToppings(self, toAdd):
      self.toppings.append(toAdd)

  def removeToppings(self, toRemove):
      self.toRemove

  def changeSize(self, size):
      self.size = size
