from PizzaParlour import app
from Classes.Menu import Menu
from Classes.Drinks import Drinks
from Classes.Order import Order
from Classes.Pizza import Pizza
from Classes.Parlour import Parlour
from main import *

def test_pizza():
    response = app.test_client().get('/pizza')

    assert response.status_code == 200
    assert response.data == b'Welcome to Pizza Planet!'

# Main CLI tests
def test_valid_num():
    check = valid_num_input('10')
    check2 = valid_num_input('Bleh')
    check3 = valid_num_input('')
    check4 = valid_num_input('-9')
    assert(check == True)
    assert(check2 == "Please enter an integer")
    assert(check3 == "Please enter a non-empty integer")
    assert(check4 == "Negative numbers are not allowed")

def test_custom_pizza_post():
    toppings = "Mushroom"
    pizza_name = "Mushroom pizza"
    check = add_custom_post(toppings, pizza_name)
    assert(check.status_code == 200)
    assert(check.text == "Pizza successfully added to menu")

def test_order_pizzas_drinks_post():
    num_pizzas = '1'
    num_drinks = '1'
    size = ['Medium']
    type = ['Pepperoni']
    toppings = ['Beef']
    drinks = ['Coke']
    check = order_pizzas_drinks_post(num_pizzas, num_drinks, size, type, toppings, drinks)
    assert(check.status_code == 200)
    # Only works if the first order
    # assert(check.text == "Order #1 successfully added. Your order cost is: $17.125")

def test_show_order_post():
    check = show_order_post('1')
    assert(check.status_code == 200)

def test_cancel_order_post():
    order_num = '1'
    check = cancel_order_post(order_num)
    assert(check.status_code == 200)
    assert(check.text == "Order successfully removed")

    order_num2 = '10'
    check2 = cancel_order_post(order_num2)
    assert(check2.status_code == 200)
    assert(check2.text == "Order you're trying to remove does not exist")

def test_show_menu_item_get():
    item = "Basil"
    check = show_menu_item_get(item)
    assert(check.status_code == 200)
    assert(check.text == "0.15")

def test_add_one_pizza_post():
    test_order_pizzas_drinks_post()
    order_to_edit = '2'
    size = 'Small'
    type = 'Pepperoni'
    toppings = 'Mushroom,Tomatoes'
    check = add_one_pizza_post(order_to_edit, size, type, toppings)
    assert(check.status_code == 200)
    assert(check.text == "New pizza successfully added")

def test_modify_pizza_post():
    what_to_edit = '1'
    order_to_edit = '2'
    num_pizza_to_update = '2'
    new_size = 'Small'
    new_type = ''
    new_toppings = ''
    
    check = modify_pizza_post(what_to_edit, order_to_edit, num_pizza_to_update, new_size, new_type, new_toppings)

    assert(check.status_code == 200)
    assert(check.text == "Changes succcefully made")

def test_delete_pizza_post():
    order_to_edit = '2'
    pizza_num = '2'
    check = delete_pizza_post(order_to_edit, pizza_num)
    assert(check.status_code == 200)
    assert(check.text == "Pizza successfully removed")

# Class Menu and drink  and pizza tests #
def test_get_pizza_price():
    menu = Menu()
    i = menu.get_pizza_price("Pepperoni")
    assert(i == 12)

def test_get_drink_price():
    menu = Menu()
    i = menu.get_drink_price("Coke")
    assert(i == 1.5)

def test_valid_pizza():
    menu = Menu()
    assert(menu.check_valid_pizza("Pepperoni") == True)

def test_add_pizza_type():
    menu = Menu()
    result = menu.add_pizza_type("Pineapple", ["Chicken"])
    assert(result == "Pizza successfully added to menu")

def test_drink():
    menu = Menu()
    drink = Drinks("Coke")
    drink.change_type("Water")
    assert(drink.type == "Water")
    assert(drink.get_cost(menu) == 2)
    assert(drink.get_drink()== {'type':'Water'})

def test_create_pizza():
    pizza = Pizza("Medium", "Neapolitan", ["Chicken"])
    menu = Menu()
    assert(pizza.make_pizza() == pizza)
    assert (pizza.get_pizza() == {'size':"Medium", 'type':"Neapolitan", 'toppings':['Chicken']})
    assert(pizza.get_cost(menu)== 14.125)

    pizza.change_toppings(["Chicken", "Mushroom", "Olives"])
    pizza.change_type("Pepperoni")
    assert (pizza.get_pizza() == {'size':"Medium", 'type':"Pepperoni", 'toppings':["Chicken", "Mushroom", "Olives"]})

# Order tests #
def test_order_add_remove():
    order = Order(1)
    assert(order.cost == 0)
    assert(order.pizza_num == 0)

    pizza1 = Pizza("Small", "Pepperoni", "Basil")
    pizza2 = Pizza("Large","Vegetarian","Olives")
    order.add_pizza(pizza1)
    order.add_pizza(pizza2)
    assert(order.num_pizzas == 2)

    order.remove_pizza("2")
    assert(order.num_pizzas == 1)

    order.change_type("Large",1)
    assert(order.pizzas["1"].type == "Large")

#Parlour tests#
def test_parlour():
    p = Parlour()
    valid_pizza = p.check_valid_pizza("Small","Vegetarian",["Basil","Beef"])
    invalid_pizza = p.check_valid_pizza("Large","poop","")

    assert(valid_pizza == True)
    assert(invalid_pizza == False)

    valid_drink = p.check_valid_drink("Coke")
    assert(valid_drink == True)
