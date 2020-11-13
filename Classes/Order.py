from Classes.Pizza import Pizza
from Classes.Drinks import Drinks

class Order:
  def __init__(self, order_num):
    self.order_num = order_num
    self.cost = 0 # Default

    #Used for the creation of pizza in dictionary
    self.pizza_num = 0
    self.drink_num = 0

    #Used to count the pizzas and dirnks
    self.num_pizzas = 0
    self.num_drinks = 0

    self.pizzas = {}
    self.drinks = {}

  def add_pizza(self, pizza):
      self.pizza_num += 1
      self.num_pizzas += 1

      self.pizzas[str(self.pizza_num)] = pizza

  def remove_pizza(self, pizza_num):
      if pizza_num in self.pizzas:
          del self.pizzas[str(pizza_num)]
          self.num_pizzas -= 1
          return "Pizza successfully removed"
      else:
          return "Pizza you're trying to remove does not exist"

  def change_size(self, size, pizza_num):
      self.pizzas[str(pizza_num)].change_size(size)

  def change_type(self, type, pizza_num):
      self.pizzas[str(pizza_num)].change_type(type)

  def change_toppings(self, toppings, pizza_num):
      self.pizzas[str(pizza_num)].change_toppings(toppings)

  def add_drink(self, drink):
      self.drink_num += 1
      self.num_drinks += 1

      self.drinks[str(self.drink_num)] = drink

  def remove_drink(self, drink_num):
      if drink_num in self.drinks:
          del self.drinks[str(drink_num)]
          self.num_drinks -= 1
          return "Drink successfully removed"
      else:
          return "Drink you're trying to remove does not exist"

  def change_drink(self, drink_type, drink_num):
      self.drinks[str(drink_num)].change_type(drink_type)

  def get_order(self, menu):
      order_temp = {}
      self.cost = self.get_cost(menu)
      temp_pizzas = {}
      for pizza in self.pizzas:
          temp_pizzas[str(pizza)] = self.pizzas[str(pizza)].get_pizza();

      order_temp["pizzas"] = temp_pizzas
      temp_drinks = {}
      for drink in self.drinks:
          temp_drinks[str(drink)] = self.drinks[str(drink)].get_drink();

      order_temp["drinks"] = temp_drinks
      order_temp["cost"] = self.cost
      return order_temp;

  def get_cost(self, menu):
      cost = 0
      for pizza in self.pizzas.values():
          cost += pizza.get_cost(menu)

      for drink in self.drinks.values():
          cost += drink.get_cost(menu)

      return cost
