# Print a welcome message for the tip calculator
print("Welcome to the tip calculator!")

# Ask the user for the total bill amount and convert it to a float for calculations
bill = float(input("What was the total bill?\n$"))

# Ask the user for the tip percentage they want to give (10%, 12%, or 15%) and convert it to an integer
tip = int(input("What percentage tip would you like to give? 10, 12, 15?\n"))

# Ask the user for the number of people splitting the bill and convert it to an integer
people = int(input("How many people to split the bill?\n"))

# Calculate the final amount each person should pay
# Step 1: Calculate the total tip amount by multiplying the bill by (tip/100)
# Step 2: Add the tip to the bill
# Step 3: Divide the total by the number of people and round the result to 2 decimal places
final_amount = round((bill + (bill * (tip / 100))) / people, 2)

# Print the final amount each person needs to pay, formatted to 2 decimal places
print(f"Each person should pay: ${final_amount:.2f}")