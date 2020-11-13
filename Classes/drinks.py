from Classes.menu import Menu

class Drinks:
  def __init__(self, type):
    self.type = type

  def change_type(self, type):
     self.type = type

  def get_cost(self, menu):
      return menu.drinks.get(self.type)

  def get_drink(self):
      drink_temp = {}
      drink_temp["type"] = self.type
      return drink_temp
