from Classes.Menu import Menu

class Drinks:
  def __init__(self, type):
    self.type = type

  # Change drink type
  def change_type(self, type):
     self.type = type

  # Get drink cost
  def get_cost(self, menu):
      return menu.drinks.get(self.type)

  # Get drink in dict form
  def get_drink(self):
      drink_temp = {}
      drink_temp["type"] = self.type
      return drink_temp
