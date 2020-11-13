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
          if (topping != ""):
              toppingCost += menu.toppings.get(topping)

      cost = baseCost + toppingCost
      cost = cost * menu.sizes[self.size]

      return cost

  # Might bot
  def change_size(self, size):
      self.size = size

  def change_type(self, type):
      self.type = type

  def change_toppings(self, toppings):
      self.toppings = toppings

  def get_pizza(self):
      pizza_temp = {}
      pizza_temp['size'] = self.size
      pizza_temp['type'] = self.type
      pizza_temp['toppings'] = self.toppings
      return pizza_temp
