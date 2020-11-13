from PizzaParlour import app
from Classes.Menu import Menu
from Classes.Drinks import Drinks
from Classes.Order import Order
from Classes.Pizza import Pizza
from Classes.Parlour import Parlour

def test_pizza():
    response = app.test_client().get('/pizza')

    assert response.status_code == 200
    assert response.data == b'Welcome to Pizza Planet!'

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
