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
      self.sizes = {
          "Small" : 1,
          "Medium": 1.25,
          "Large": 1.5
      }

  def check_valid_pizza(self, pizzaType):
      return pizzaType in self.pizzas and pizzaType != ""

  def check_valid_drink(self, drinkType):
      return drinkType in self.drinks and drinkType != ""

  def check_valid_toppings(self, toppingType):
      return toppingType in self.toppings

  def check_valid_sizes(self, size):
      return size in self.sizes

  def get_menu(self):
      menu_temp = {}
      menu_temp["pizzas"] = self.pizzas
      menu_temp["pizzasPrep"] = self.pizzasPrep
      menu_temp["drinks"] = self.drinks
      menu_temp["toppings"] = self.toppings
      menu_temp["sizes"] = self.sizes
      return menu_temp

  def get_pizza_price(self, pizzaType):
      return self.pizzas[pizzaType]

  def get_drink_price(self, drinkType):
      return self.drinks[drinkType]

  def get_topping_price(self, toppingType):
      return self.toppings[toppingType]

  def add_pizza_type(self, pizza, toppings):
       cost = 10

       for topping in toppings:
           if topping in self.toppings:
               cost += self.toppings[topping]
           else:
               return "Topping not found"

       self.pizzas[str(pizza)] = cost
       self.pizzasPrep[str(pizza)] = toppings

       return "Pizza successfully added to menu"
