# Day 12: Beginner - Number Guessing Game

## Topics Covered

### 1. Functions with Outputs
- Created functions that return values to improve code structure.
- Used functions to check user guesses and provide feedback dynamically.

### 2. User Input Handling
- Implemented validation to ensure users enter only valid inputs (difficulty selection and numeric guesses).

### 3. Loops & Conditionals
- Used `while` loops to control game flow.
- Applied conditional statements to guide user interactions and game progress.

### 4. Random Module
- Utilized Python’s `random` module to generate a secret number between 1 and 100.

### 5. Project: Number Guessing Game
- Built a game where users guess a randomly generated number within a limited number of attempts.

---

## Project: Number Guessing Game

### Key Features

1. **Difficulty Levels**
   - Players can choose between **"easy"** (10 attempts) or **"hard"** (5 attempts).

2. **Dynamic Feedback**
   - The program informs players if their guess is **too high** or **too low** after each attempt.

3. **Attempt Tracking**
   - The game tracks remaining attempts and informs users after each guess.
   - Ends when the player guesses correctly or runs out of attempts.

4. **Input Validation**
   - Ensures users enter valid numerical guesses.
   - Handles invalid difficulty inputs by prompting again.

5. **Win/Loss Handling**
   - Displays a success message if the player guesses correctly.
   - Ends with a failure message when attempts reach zero.

---

### Key Learnings

1. **Function-Based Design**
   - Encapsulated logic into functions to make the code cleaner and reusable.

2. **User Experience Enhancements**
   - Provided clear prompts and dynamic feedback to engage the player.

3. **Loop Control & Game Logic**
   - Managed game flow using loops and conditions.

4. **Randomization**
   - Used `random.randint()` to generate unpredictable numbers for each session.

---

### Improvements for Future Versions

1. **Multiple Rounds**
   - Allow players to restart the game without restarting the script.

2. **Scoring System**
   - Track wins and losses for multiple rounds.

3. **Customizable Difficulty**
   - Let users define their own difficulty levels (e.g., select a custom number of attempts).

4. **Error Handling Enhancements**
   - Improve handling of non-numeric inputs for a more robust experience.

5. **GUI Integration**
   - Convert the game into a simple GUI-based application using `tkinter` or `PyQt`.

---

### Summary

The **Number Guessing Game** is a great beginner-friendly project to practice **functions, loops, conditionals, and user input handling**. It provides a fun way to apply programming concepts while focusing on user experience and game logic. Future enhancements can make the game more engaging, interactive, and adaptable to different difficulty levels.
