# ☕ Day 15: Intermediate - Coffee Machine Project  

## Topics Covered  

### 1. Functions & Code Structuring  
- Used functions to encapsulate logic for better readability and reusability.  
- Implemented helper functions to handle checking resources, processing payments, and making coffee.  

### 2. Dictionaries for Data Management  
- Utilized dictionaries to store menu items, ingredient requirements, and costs.  
- Created a separate dictionary to track available resources.  

### 3. User Input Handling  
- Allowed users to select a drink, view a report, or turn off the machine.  
- Ensured only valid commands (`"espresso"`, `"latte"`, `"cappuccino"`, `"report"`, `"off"`) were accepted.  

### 4. Mathematical Operations  
- Implemented calculations to handle coin input and determine if a user has inserted enough money.  
- Managed resource subtraction after each successful coffee transaction.  

### 5. Loop Control & Game Flow  
- Used a `while` loop to keep the machine running until the user turns it off.  
- Ensured resources and money were updated dynamically after each purchase.  

---

## Project: Coffee Machine Simulator  

### Key Features  

1. **Menu & Resource Management**  
   - Stores available drinks and their respective ingredient requirements.  
   - Keeps track of remaining resources dynamically.  

2. **User Commands**  
   - Users can order coffee, check available resources, or turn off the machine.  
   - The machine processes transactions and updates resources accordingly.  

3. **Payment Processing**  
   - Users insert coins (quarters, dimes, nickels, pennies) to pay for coffee.  
   - If the payment is insufficient, the transaction is canceled, and money is refunded.  

4. **Resource Availability Check**  
   - Before making a drink, the machine verifies that enough ingredients are available.  
   - If any ingredient is insufficient, it notifies the user and does not proceed.  

5. **Game-Like Flow**  
   - The machine continuously runs until manually turned off.  
   - Drinks can be purchased in succession, and the report updates dynamically.  

---

## Key Learnings  

1. **Function-Based Design**  
   - Encapsulated coffee-making logic within functions to reduce redundancy.  
   - Created modular functions for checking resources, processi
