def add(n1, n2):
    """Adds two numbers and returns the result."""
    return n1 + n2

def multiply(n1, n2):
    """Multiplies two numbers and returns the result."""
    return n1 * n2

def subtract(n1, n2):
    """Subtracts the second number from the first and returns the result."""
    return n1 - n2

def divide(n1, n2):
    """Divides the first number by the second and returns the result."""
    return n1 / n2

# Dictionary mapping operation symbols to their respective functions
Operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

def calculator():
    """
    Runs a simple calculator program that supports addition, subtraction,
    multiplication, and division. Allows continuous calculations or restarting
    with a new calculation.
    """
    result = None  # Initialize result to None for the first calculation

    while True:
        # If no prior result, ask for the first number
        if result is None:
            first_number = float(input("What is the first number? "))
        else:
            first_number = result  # Use the previous result for the next calculation

        # Display available operations
        for symbol in Operations:
            print(symbol)

        # Prompt user to select an operation
        select_operation = input("Select an Operation: ")
        while select_operation not in Operations:
            print("Invalid operation. Please select a valid one.")
            select_operation = input("Select an operation: ")

        # Ask for the next number and handle division by zero
        while True:
            second_number = float(input("What is the next number? "))
            if select_operation == "/" and second_number == 0:
                print("Error: Division by zero is not allowed. Please enter a valid number.")
            else:
                break

        # Perform the selected operation
        result = Operations[select_operation](first_number, second_number)
        print(f"{first_number} {select_operation} {second_number} = {result}")

        # Ask the user whether to continue, restart, or exit
        while True:
            again = input(f"Type 'y' to continue calculating with {result}, "
                          f"or type 'n' to start a new calculation or 'x' to exit the calculator: \n").lower()

            if again == "y":  # Continue with the current result
                break

            elif again == "n":  # Restart with a new calculation
                result = None
                print("\n" * 40)  # Clear the screen for a fresh start
                break

            elif again == "x":  # Exit the calculator
                print("Thanks for using the calculator!")
                exit()

            else:
                # Handle invalid input for the continuation prompt
                print(f"Invalid Selection!")

# Start the calculator program
calculator()
