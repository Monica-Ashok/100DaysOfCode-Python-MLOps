# Day 03 - Control Flow and Logical Operators

## Key Concepts Covered:

### 1. **Control Flow with if / else and Conditional Operators**
- The `if / else` structure allows programs to make decisions based on conditions.
- Conditional operators (`==`, `!=`, `>`, `<`, `>=`, `<=`) are used to evaluate expressions.

### 2. **Modulo Operator**
- The `%` operator returns the remainder of a division.
- Useful for tasks like checking divisibility (e.g., `number % 2 == 0` for even numbers).

### 3. **Nested if Statements and elif Statements**
- `if` statements can be nested within each other for more complex decision-making.
- `elif` (else if) allows multiple conditions to be evaluated sequentially.

### 4. **Multiple If Statements in Succession**
- Unlike `if...elif...else`, successive `if` statements evaluate all conditions independently.

### 5. **Logical Operators**
- Combine multiple conditions using logical operators:
  - `and`: All conditions must be true.
  - `or`: At least one condition must be true.
  - `not`: Negates a condition (e.g., `not True` is `False`).

---

## Project 03 - Treasure Island

### Project Description:
I built a simple and fun text-based adventure game where players make decisions to find hidden treasure. The game uses conditional logic and control flow to determine outcomes based on player input.

---

### Project Logic
1. **Introduction**:
   - Welcome the player to "Treasure Island" and explain their mission.

2. **Scene 1: The Crossroads**:
   - Prompt the player to choose between "left" or "right."
   - If they choose "right," the game ends with a message about falling into a hole.
   - If they choose "left," they proceed to the next scene.

3. **Scene 2: The Riverbank**:
   - The player chooses to either "swim" or "wait."
   - If they choose "swim," they are attacked by trout, and the game ends.
   - If they choose "wait," they proceed to the final scene.

4. **Scene 3: The Doors of Fate**:
   - The player selects one of three doors: "red," "blue," or "yellow."
   - "Red" door: Burned by fire.
   - "Blue" door: Eaten by beasts.
   - "Yellow" door: Treasure found; player wins!
   - Any other input results in a game over.