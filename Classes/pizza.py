from Classes.menu import Menu

class Pizza:
  def __init__(self, size, type, toppings):
    self.size = size
    self.type = type
    self.toppings = toppings

  def make_pizza(self):
      return self

  def get_cost(self, menu):
      cost = 0
      # Switch based on type + toppings + size for cost
      baseCost = menu.pizzas.get(self.type)
      toppingCost = 0
      for topping in self.toppings:
          toppingCost += menu.toppings.get(topping)

      return baseCost + toppingCost

  # Might bot
  def add_toppings(self, toAdd):
      self.toppings.append(toAdd)

  def remove_toppings(self, toRemove):
      self.toRemove

  def change_size(self, size):
      self.size = size
