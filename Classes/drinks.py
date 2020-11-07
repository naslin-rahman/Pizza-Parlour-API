class Drinks:
  def __init__(self, type):
    self.type = type

    # Switch based on type for cost
    self.cost = 0

  def getCost(self):
      return self.cost
