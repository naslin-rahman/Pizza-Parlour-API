class Order:
  def __init__(self, ordernum):
    self.ordernum = ordernum
    self.cost = 0 # Default
    self.pizzas = []
    self.drinks = []

  def getCost(self):
      cost = 0
      for pizza in self.pizzas:
          cost += pizza.getCost()

      for drink in self.drinks:
          cost += drinks.getCost()
