# ☕ Day 16: Intermediate - Object-Oriented Programming (OOP)

## 🔹 Overview
In this challenge, I worked with **pre-built OOP-based classes** and focused on modifying the **Coffee Machine** functionality to integrate with the given OOP structure.

### 🏗 What Was Provided?
I was given **four pre-built classes**:
1. **MenuItem** – Defines drink properties (name, cost, ingredients).
2. **Menu** – Manages available drinks and retrieves menu items.
3. **CoffeeMaker** – Handles resource tracking and coffee-making.
4. **MoneyMachine** – Manages payments and tracks profit.

### 🔧 What I Did?
- Integrated the **Coffee Machine logic** into the existing OOP framework.
- Ensured **correct interactions** between `Menu`, `CoffeeMaker`, and `MoneyMachine`.
- Implemented **resource checks**, **user input handling**, and **payment processing** using OOP principles.
- **Refactored** procedural code to fit into **OOP classes and methods**.

---

## 📌 Key Learnings

### ✅ 1. Working with Pre-Built OOP Structures
- Instead of writing everything from scratch, I learned to **extend and integrate** existing OOP-based code.
- Understood how **classes communicate** through method calls and object instances.

### ✅ 2. Implementing Encapsulation & Composition
- Separated **data (attributes)** and **behavior (methods)** into appropriate classes.
- Ensured **CoffeeMaker** and **MoneyMachine** only handled their respective tasks.

### ✅ 3. Managing Dependencies Between Classes
- Used `Menu.find_drink(order_name)` to fetch the correct `MenuItem` object.
- Passed `MenuItem` instances to `CoffeeMaker.is_resource_sufficient()` for validation.
- Integrated `MoneyMachine.make_payment(cost)` before making coffee.

---

## 🔮 Possible Improvements
- **Save order history** – Track user purchases in a file/database.
- **Custom drink options** – Allow users to modify ingredient quantities.
- **GUI Implementation** – Convert to a graphical coffee machine using `tkinter` or `PyGame`.

---

### 📂 Coffee Machine Documentation

#### MenuItem Class
##### Attributes:
- name
(str) The name of the drink.
e.g. “latte”
- cost
(float) The price of the drink.
e.g 1.5
- ingredients
(dictionary) The ingredients and amounts required to make the drink.
e.g. {“water”: 100, “coffee”: 16}

#### Menu Class
##### Methods:
- get_items()
Returns all the names of the available menu items as a concatenated string.
e.g. “latte/espresso/cappuccino”
- find_drink(order_name)
Parameter order_name: (str) The name of the drinks order.
Searches the menu for a particular drink by name. Returns a MenuItem object if it exists,
otherwise returns None.

#### CoffeeMaker Class
##### Methods:
- report()
Prints a report of all resources.
e.g.
Water: 300ml
Milk: 200ml
Coffee: 100g
- is_resource_sufficient(drink)
Parameter drink: (MenuItem) The MenuItem object to make.
Prints a message if ingredients are insufficient.
Returns True when the drink order can be made, False if ingredients are insufficient.
e.g.
True
- make_coffee(order)
Parameter order: (MenuItem) The MenuItem object to make.
Deducts the required ingredients from the resources.

#### MoneyMachine Class
##### Methods:
- report()
Prints the current profit
e.g.
Money: $0
- make_payment(cost)
Parameter cost: (float) The cost of the drink.
Returns True when payment is accepted, or False if insufficient.
e.g. False
