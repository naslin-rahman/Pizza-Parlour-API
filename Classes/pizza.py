class Pizza:
  def __init__(self, size, type, toppings):
    self.size = size
    self.type = type
    self.toppings = toppings

    self.cost = getCost(self)

  def makePizza(self):
      return self

  def getCost(self):
      cost = 0
      # Switch based on type + toppings + size for cost

      return cost
