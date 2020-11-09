class Menu:
  def __init__(self):
      self.pizzas = {
          "Pepperoni": 12,
          "Magherita": 9,
          "Vegetarian": 11,
          "Neapolitan": 11
        }
      self.pizzasPrep = {
          "Pepperoni": ["Pepperoni"],
          "Magherita": ["Basil"],
          "Vegetarian": ["Tomatoes", "Mushroom", "Jalapenos"],
          "Neapolitan": ["Tomatoes"]
        }

      self.drinks = {
          "Coke" : 1.5,
          "Diet Coke" : 1.5,
          "Coke Zero" : 1.5,
          "Pepsi" : 1.5,
          "Diet Pepsi" : 1.5,
          "Dr. Pepper" : 1.5,
          "Water" : 2,
          "Juice" : 1
      }
      self.toppings = {
          "Basil" : 0.15,
          "Olives" : 0.25,
          "Tomatoes" : 0.25,
          "Mushroom" : 0.25,
          "Jalapenos" : 0.25,
          "Chicken" : 0.3,
          "Beef" : 0.5,
          "Pepperoni": 0.35
      }

  def get_menu(self):
      menu_temp = {}
      menu_temp["pizzas"] = self.pizzas
      menu_temp["pizzasPrep"] = self.pizzasPrep
      menu_temp["drinks"] = self.drinks
      menu_temp["toppings"] = self.toppings
      return menu_temp

  def get_pizza_price(self, pizzaType):
      return self.pizzas[pizzaType]

  def get_drink_price(self, drinkType):
      return self.drinks[drinkType]

  def get_topping_price(self, toppingType):
      return self.toppings[toppingType]

  def add_pizza(self, pizza, toppings):
       cost = 10

       for topping in toppings:
           cost += self.menu.toppings[topping]
           
       self.pizzas[newPizza] = cost
       self.pizzasPrep[newPizza] = toppings
