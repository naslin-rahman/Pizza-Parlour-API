from Classes.menu import Menu

class Drinks:
  def __init__(self, type):
    self.type = type

  def change_type(self, type):
     self.type = type

  def get_cost(self, menu):
      return menu.drinks.get(self.type)
