# Pizza Parlour API

Run the main Flask module by running `python3 PizzaParlour.py`

Run unit tests with coverage by running `pytest --cov-report term --cov=. tests/unit_tests.py`

## Pair Programming
### Show menu and item price feature (Driver: Naslin, Navigator: Allison)

To implement these features I had to first prompt the user in the CLI (in main.py) if they entered the command “menu”. Then I added a prompt asking the user if they wanted to to view the entire menu (to which they would type “yes” or not in which they would type “no” and then can enter the name of the item (pizza, drink, topping) they would like to see the price for. Then I added the appropriate get routes in PizzaParlour.py and implemented them by calling the appropriate methods in Parlour.py. I also added unit tests to make sure the right menu object and price was returned.

Note: Pair programmed unit tests for show menu/item price feature are in commit 67ad954. (Forgot to add pair programmed message in commit)

#### Pros and Cons:
In my opinion, pair programming was a wonderful experience. We were both able to share ideas on how to implement the features. On the downside it is very time consuming compared to programming by oneself.


### Adding custom pizza combos (Driver: Allison, Navigator: Naslin)
Programmed adding custom pizza combos onto the menu. First implemented CI to get a better idea of how data would be structured based on our design of the user experience. Then added the get route to PizzaParlour and implemented the method in the Menu Class. Worked with the navigator to come up with the design of an overall parlour and menu object for interaction. Unit tests were pair programmed with help from the navigator since she had more prior experience with unit testing. The specific method for this feature is test_custom_pizza_json() in unit_test()

Note: Pair programmed unit tests are in commit da5aba5. (Forgot to add pair programmed message in commit)
#### Pros and Cons:
What I liked about this experience was getting advice and input from someone who knew more than me and could help. However, what I disliked was that at times when deciding the file structure, there can be multiple ideas which slow down the process.

## Program Design
At the lowest level, we have classes for Drinks, Pizzas and the Menu that store the basic attributes of a single item. Then since there can be multiple instances of these items in one order, we decided to also include an Order class to manage all the pizzas and drinks that could be in an order. We also implemented the builder design pattern in the class OrderBuilder. By taking in just strings from the user input, OrderBuilder helps put together all the different components that go into an order.

The PizzaParlour.Py file mainly contains the implementations of all the routes, and Parlour class was made to keep most of the logic separate from this file. The PizzaParlour.py file does not interact with any class other than Parlour. As more features were added, MenuManager and OrderManager classes were added to keep the implementation of non related methods in parlour separate.

## App Instructions
Dependencies: To make sure things run smoothly make sure that flask, pytest, pytest-cov, and coverage. Or run the following commands for set up:
- `pip3 install flask`
- `pip3 install request`
- `pip3 install requests`
- `pip3 install pytest`
- `pip3 install pytest-cov`
- `pip3 install coverage`

To use our app, the user can enter the following steps:
Run the main Flask module by running `python3 PizzaParlour.py`
To use the CI interface to interact with the Flask module, run `python3 main.py` in a **seperate terminal** 
These are the commands you can issue:
**Type the number** of the action you would like to perform
- [1] Show an order
- [2] Cancel an order
- [3] Show menu
- [4] Add a custom pizza type
- [5] Order
- [6] Make an update to an order
- [7] Change the price of an item
- [8] Finish ordering (onto delivery)

Run unit tests with coverage by running `coverage run -m pytest --cov-report term --cov=. tests/unit_tests.py`

**Things to keep in mind:**
- Valid pizza sizes, types, and toppings are the examples shown in the assignment doc. Same applies to the drink types. To see in more detail, go to the show menu option in the cli.
- When entering toppings, separate different toppings with a single comma. Spaces will cause issues due to how we split the string into separate toppings. 
**Ok**: Mushroom,Basil,Tomatoes **Not OK**: Mushroom, Basil, Tomatoes
- When entering method of delivery please type one of the following (Uber Eats, Foodora, Pickup)      

## Code Craftsmanship 
We both used an extension in Visual Studio Code called "Prettier code formatter" to format the code effectively. While the other partner who mainly worked in atom, used the extension linter-pycodestyle to help with formatting.



