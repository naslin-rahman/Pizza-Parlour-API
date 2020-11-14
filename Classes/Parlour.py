from Classes.Pizza import Pizza
from Classes.Drinks import Drinks
from Classes.Order import Order
from Classes.Menu import Menu
from Classes.OrderBuilder import OrderBuilder
from Classes.MenuManager import MenuManager
from Classes.OrderManager import OrderManager
import json

class Parlour:
    def __init__(self):
        self.menu_manager = MenuManager()
        self.order_manager = OrderManager()

    ##### Methods that deal with orders such as creation/modifying an order #####
    ##### *** More detail in each manager
    def check_valid_pizza(self, pizza_size, pizza_type, pizza_toppings):
        menu = self.menu_manager.menu_get()
        return self.order_manager.check_valid_pizza(pizza_size, pizza_type, pizza_toppings, menu)

    def check_valid_drink(self, drink_type):
        menu = self.menu_manager.menu_get()
        return self.order_manager.check_valid_drink(drink_type, menu)

    def new_order(self, num_pizzas, num_drinks, pizza_size, pizza_type, pizza_toppings, drink_type):
        menu = self.menu_manager.menu_get()
        return self.order_manager.new_order(num_pizzas, num_drinks, pizza_size, pizza_type, pizza_toppings, drink_type, menu)

    def modify_pizza(self, pizza_size, pizza_type, pizza_toppings, order_num, pizza_num, what_to_edit):
        menu = self.menu_manager.menu_get()
        return self.order_manager.modify_pizza(pizza_size, pizza_type, pizza_toppings, order_num, pizza_num, what_to_edit, menu)

    def add_pizza(self, pizza_size, pizza_type, pizza_toppings, order_num):
        menu = self.menu_manager.menu_get()
        return self.order_manager.add_pizza(pizza_size, pizza_type, pizza_toppings, order_num, menu)

    def delete_pizza(self, pizza_num, order_num):
        return self.order_manager.delete_pizza(pizza_num, order_num)

    def modify_drink(self, drink_type, drink_num, order_num):
        menu = self.menu_manager.menu_get()
        return self.order_manager.modify_drink(drink_type, drink_num, order_num, menu)

    def add_drink(self, drink_type, order_num):
        menu = self.menu_manager.menu_get()
        return self.order_manager.add_drink(drink_type, order_num, menu)

    def delete_drink(self, drink_num, order_num):
        return self.order_manager.delete_drink(drink_num, order_num)

    def cancel_order(self, order_num):
        return self.order_manager.cancel_order(order_num)

    def get_order(self, order_num):
        menu = self.menu_manager.menu_get()
        return self.order_manager.get_order(order_num, menu)

    ##### Methods that deal with menus such as getting the menu or modifying it #####
    def get_menu(self):
        return self.menu_manager.get_menu()

    def add_pizza_to_menu(self, toppings_str, new_pizza):
        return self.menu_manager.add_pizza_to_menu(toppings_str, new_pizza)

    def menu_get(self):
        return self.menu_manager.menu_get()

    def change_item_price(self, item, new_price):
        return self.menu_manager.change_item_price(item, new_price)
