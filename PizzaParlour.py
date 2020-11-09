from flask import Flask
from Classes.parlourInterface import ParlourInterface

app = Flask("Assignment 2")
parlour = ParlourInterface()

@app.route('/pizza')
def welcome_pizza():
    return 'Welcome to Pizza Planet!'

@app.route('/menu')
def menu():
    # Return the entire menu
    menu = parlour.get_menu()
    return parlour.get_menu()

@app.route('/menu/price', methods = ['GET'])
def get_item_price(item_name):
    # TODO
    return 'This is the menu item price'

if __name__ == "__main__":
    app.run(debug = True)
