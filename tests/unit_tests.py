from PizzaParlour import app
from Classes.Menu import Menu
from Classes.Drinks import Drinks
from Classes.Order import Order
from Classes.Pizza import Pizza
from Classes.Parlour import Parlour
from Classes.OrderBuilder import OrderBuilder
from Classes.OrderManager import OrderManager
from CLIRequestsAndJson.RequestMethods import *
from CLIRequestsAndJson.JsonMethods import *
from main import *

def test_pizza():
    response = app.test_client().get('/pizza')

    assert response.status_code == 200
    assert response.data == b'Welcome to Pizza Planet!'

##### Main CLI tests #####
def test_menu():
    p = Parlour()
    response = app.test_client().get('/menu')

    assert response.status_code == 200

def test_menu_item():
    item = "Pepperoni"
    json_string = show_menu_item_json(item)
    response = app.test_client().get('/menu/price', json=json_string)
    assert response.status_code == 200
    assert response.data == b'12'

def test_valid_num():
    check = valid_num_input('10')
    check2 = valid_num_input('Bleh')
    check3 = valid_num_input('')
    check4 = valid_num_input('-9')
    assert(check == True)
    assert(check2 == "Please enter an integer")
    assert(check3 == "Please enter a non-empty integer")
    assert(check4 == "Negative numbers are not allowed")

def test_custom_pizza_json():
    toppings = "Mushroom"
    pizza_name = "Mushroom pizza"
    json_string = add_custom_json(toppings, pizza_name)
    check = app.test_client().post('/menu/add_pizza_type', json=json_string)
    assert(check.status_code == 200)
    assert(check.data == b"Pizza successfully added to menu")

def test_order_pizzas_drinks_json():
    num_pizzas = '1'
    num_drinks = '1'
    size = ['Medium']
    type = ['Pepperoni']
    toppings = ['Beef']
    drinks = ['Coke']
    json_string = order_pizzas_drinks_json(num_pizzas, num_drinks, size, type, toppings, drinks)
    check = app.test_client().post('/new_order', json=json_string)
    assert(check.status_code == 200)
    # Only works if the first order - Too specific
    # assert(check.data == b"Order #1 successfully added. Your order cost is: $17.125")

def test_show_order_json():
    json_string = show_order_json('1')
    check = app.test_client().post('/show_order', json=json_string)
    assert(check.status_code == 200)

def test_cancel_order_json():
    order_num = '1'
    json_string = cancel_order_json(order_num)
    check = app.test_client().post('/cancel_order', json=json_string)
    assert(check.status_code == 200)
    assert(check.data == b"Order successfully removed")

    order_num2 = '10'
    json_string2 = cancel_order_json(order_num2)
    check2 = app.test_client().post('/cancel_order', json=json_string2)
    assert(check2.status_code == 200)
    assert(check2.data == b"Order you're trying to remove does not exist")

def test_show_menu_item_json():
    item = "Basil"
    json_string = show_menu_item_json(item)
    check = app.test_client().get('/menu/price', json=json_string)
    assert(check.status_code == 200)
    assert(check.data == b"0.15")

def test_add_one_pizza_json():
    test_order_pizzas_drinks_json()
    order_to_edit = '2'
    size = 'Small'
    type = 'Pepperoni'
    toppings = 'Mushroom,Tomatoes'
    json_string = add_one_pizza_json(order_to_edit, size, type, toppings)
    check = app.test_client().post('/modify_order/add_pizza', json=json_string)

    assert(check.status_code == 200)
    assert(check.data == b"New pizza successfully added")

def test_modify_pizza_json_type1():
    # Size edit
    what_to_edit = '1'
    order_to_edit = '2'
    num_pizza_to_update = '2'
    new_size = 'Small'
    new_type = ''
    new_toppings = ''

    json_string = modify_pizza_json(what_to_edit, order_to_edit, num_pizza_to_update, new_size, new_type, new_toppings)
    check = app.test_client().post('/modify_order/modify_pizza', json=json_string)

    assert(check.status_code == 200)
    assert(check.data == b"Changes succcefully made")

def test_modify_pizza_json_type2():
    # Type Edit
    what_to_edit2 = '2'
    order_to_edit2 = '2'
    num_pizza_to_update2 = '2'
    new_size2 = ''
    new_type2 = 'Vegetarian'
    new_toppings2 = ''

    json_string2 = modify_pizza_json(what_to_edit2, order_to_edit2, num_pizza_to_update2, new_size2, new_type2, new_toppings2)
    check2 = app.test_client().post('/modify_order/modify_pizza', json=json_string2)

    assert(check2.status_code == 200)
    assert(check2.data == b"Changes succcefully made")

def test_modify_pizza_json_type3():
    # Toppings Edit
    what_to_edit3 = '3'
    order_to_edit3 = '2'
    num_pizza_to_update3 = '2'
    new_size3 = ''
    new_type3 = ''
    new_toppings3 = 'Tomatoes,Mushroom,Basil,Pepperoni'

    json_string3 = modify_pizza_json(what_to_edit3, order_to_edit3, num_pizza_to_update3, new_size3, new_type3, new_toppings3)
    check3 = app.test_client().post('/modify_order/modify_pizza', json=json_string3)

    assert(check3.status_code == 200)
    assert(check3.data == b"Changes succcefully made")

def test_delete_pizza_json():
    order_to_edit = '2'
    pizza_num = '2'
    json_string = delete_pizza_json(order_to_edit, pizza_num)
    check = app.test_client().post('/modify_order/remove_pizza', json=json_string)

    assert(check.status_code == 200)
    assert(check.data == b"Pizza successfully removed")

def test_add_one_drink_json():
    order_to_edit = '2'
    new_drink = 'Coke'
    json_string = add_one_drink_json(order_to_edit, new_drink)
    check = app.test_client().post('/modify_order/add_drink', json=json_string)

    assert(check.status_code == 200)
    assert(check.data == b"New drink successfully added")

def test_modify_drink_json():
    order_to_edit = '2'
    num_drink_to_update = '2'
    new_drink = 'Pepsi'
    json_string = modify_drink_json(order_to_edit, num_drink_to_update, new_drink)
    check = app.test_client().post('/modify_order/modify_drink', json=json_string)

    assert(check.status_code == 200)
    assert(check.data == b"Changes succcefully made")

def test_remove_drink_json():
    order_to_edit = '2'
    drink_num = '1'
    json_string = remove_drink_json(order_to_edit, drink_num)
    check = app.test_client().post('/modify_order/remove_drink', json=json_string)

    assert(check.status_code == 200)
    assert(check.data == b"Drink successfully removed")

    order_to_edit2 = '2'
    drink_num2 = '10'
    json_string2 = remove_drink_json(order_to_edit2, drink_num2)
    check2 = app.test_client().post('/modify_order/remove_drink', json=json_string2)

    assert(check2.status_code == 200)
    assert(check2.data == b"Drink doesn't exist")

def test_change_price_json_valid():
    item = 'Pepperoni'
    new_price = '100'
    json_string = change_price_json(item, new_price)
    check = app.test_client().post('/change_price', json=json_string)

    assert(check.status_code == 200)
    assert(check.data == b"Price successfully changed")

def test_change_price_json_invalid():
    item = 'Chocolate :D'
    new_price = '100'
    json_string = change_price_json(item, new_price)
    check = app.test_client().post('/change_price', json=json_string)

    assert(check.status_code == 200)
    assert(check.data == b"Not a valid item")

def test_delivery_json_uber():
    order_num = '2'
    address = '123 Meh Street'
    json_string = delivery_UE_json(order_num, address)
    check = app.test_client().post('/deliver/uber', json=json_string)
    assert(check.status_code == 200)
    assert(check.data == b"Your delivery is on the way!")

def test_delivery_json_foodora():
    order_num = '2'
    address = '123 Meh Street'
    json_string = delivery_F_json(order_num, address)
    check = app.test_client().post('/deliver/foodora', json=json_string)
    assert(check.status_code == 200)
    assert(check.data == b"Your delivery is on the way!")

##### Class Menu and drink  and pizza tests #####
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
    menu = Menu()
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

def test_order_manager():
    o = OrderManager()
    menu = Menu()
    assert(o.order_nums == 0)
    assert(o.orders == {})
    assert(o.check_valid_pizza("Small","Pepperoni","",menu) == True)

def test_valid_drink():
    oB = OrderBuilder()
    menu = Menu()
    i = oB.check_valid_drink("Coke", menu)
    assert(i == True)

def test_valid_pizza_object():
    oB = OrderBuilder()
    menu = Menu()
    i = oB.check_valid_pizza("Small","Pepperoni","",menu)
    assert(i == True)

def test_make_drink():
    oB = OrderBuilder()
    menu = Menu()
    assert(oB.make_drink("Water").type == "Water")

def test_make_pizza():
    oB = OrderBuilder()
    assert(oB.make_pizza("Small","Pepperoni","").type == "Pepperoni")
    assert(oB.make_pizza("Small","Pepperoni","").size == "Small")
    assert(oB.make_pizza("Small","Pepperoni","").toppings == "")

def test_make_order():
    oB = OrderBuilder()
    assert(oB.make_order(1).order_num == 1)

def test_build_order():
    oB = OrderBuilder()
    menu = Menu()
    order = oB.build_order(menu,"1","2",["Small"], ["Pepperoni"],[""],["Coke","Water"], 1)
    assert(order.order_num == 1)


#Parlour tests#
def test_parlour():
    p = Parlour()
    valid_pizza = p.check_valid_pizza("Small","Vegetarian",["Basil","Beef"])
    invalid_pizza = p.check_valid_pizza("Large","poop","")

    assert(valid_pizza == True)
    assert(invalid_pizza == False)

    valid_drink = p.check_valid_drink("Coke")
    assert(valid_drink == True)
