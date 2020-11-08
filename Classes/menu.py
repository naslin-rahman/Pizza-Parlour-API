class Menu:
  def __init__(self):
      self.pizzas = {
          "Pepperoni": 12,
          "Magherita": 9,
          "Vegetarian": 11,
          "Neapolitan": 11,
        }
      self.pizzasPrep = {
          "Pepperoni": ["Pepperoni"],
          "Magherita": ["Basil"],
          "Vegetarian": ["Tomatoes", "Mushroom", "Jalapenos"],
          "Neapolitan": ["Tomatoes"],
        }

      self.drinks = {
          "Coke" : 1.5,
          "Diet Coke" : 1.5,
          "Coke Zero" : 1.5,
          "Pepsi" : 1.5,
          "Diet Pepsi" : 1.5,
          "Dr. Pepper" : 1.5,
          "Water" : 2,
          "Juice" : 1,
      }
      self.toppings = {
          "Basil" : 0.15,
          "Olives" : 0.25,
          "Tomatoes" : 0.25,
          "Mushroom" : 0.25,
          "Jalapenos" : 0.25,
          "Chicken" : 0.3,
          "Beef" : 0.5,
          "Pepperoni": 0.35,
      }

def getMenu(self):
    menu = { self.pizzas, self.pizzasPrep, self.drinks, self.toppings}
    return menu
