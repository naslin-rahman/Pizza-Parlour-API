from Classes.menu import Menu

class Drinks:
  def __init__(self, type):
    self.type = type

  def getCost(self, menu):
      return menu.drinks.get(self.type)
