class Menu:
  def __init__(self):
      # Default Values
      self.pizzas = {
          "Pepperoni": 12,
          "Magherita": 9,
          "Vegetarian": 11,
          "Neapolitan": 11
        }
      self.pizzas_prep = {
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

      # Numbers act as multipliers for the price
      self.sizes = {
          "Small" : 1,
          "Medium": 1.25,
          "Large": 1.5
      }

  # Return if pizza_type is on the menu and isnt an empty string
  def check_valid_pizza(self, pizza_type):
      return pizza_type in self.pizzas and pizza_type != ""

  # Return if drink_type is on the menu and isnt an empty string
  def check_valid_drink(self, drink_type):
      return drink_type in self.drinks and drink_type != ""

  # Return if topping_type is on the menu and isnt an empty string
  def check_valid_toppings(self, topping_type):
      return topping_type in self.toppings and topping_type != ""

  # Return if size is on the menu and isnt an empty string
  def check_valid_sizes(self, size):
      return size in self.sizes and sizes != ""

  # Returns the menu in dict form
  def get_menu(self):
      menu_temp = {}
      menu_temp["pizzas"] = self.pizzas
      menu_temp["pizzas_prep"] = self.pizzas_prep
      menu_temp["drinks"] = self.drinks
      menu_temp["toppings"] = self.toppings
      menu_temp["sizes"] = self.sizes
      return menu_temp

  # Return price of pizza_type
  def get_pizza_price(self, pizza_type):
      return self.pizzas[pizza_type]

  # Return price of drink_type
  def get_drink_price(self, drink_type):
      return self.drinks[drink_type]

  # Return price of topping_type
  def get_topping_price(self, topping_type):
      return self.toppings[topping_type]

  # Adds topping combo to menu under pizza
  #     Checks if toppings are valid before adding
  #     Finds cost of this new pizza (Base: 10 + cost of toppings)
  # Returns whether adding was a success
  def add_pizza_type(self, pizza, toppings):
       cost = 10

       for topping in toppings:
           if topping in self.toppings:
               cost += self.toppings[topping]
           else:
               return "Topping not found"

       self.pizzas[str(pizza)] = cost
       self.pizzas_prep[str(pizza)] = toppings

       return "Pizza successfully added to menu"
