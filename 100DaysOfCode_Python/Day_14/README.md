# Day 14: Beginner - Higher or Lower Game

## Topics Covered

### 1. Functions & Code Structuring
- Used functions to encapsulate logic for readability and reusability.
- Implemented a function to check the correctness of the user's guess.

### 2. Random Module
- Utilized Python’s `random.choice()` to select accounts randomly from a dataset.

### 3. User Input Handling
- Ensured users enter only valid inputs (`"A"` or `"B"`) by prompting again on invalid input.

### 4. Loop Control & Game Flow
- Used a `while` loop to continue the game until the player makes an incorrect guess.
- Ensured that `account_a` persists while `account_b` changes for the next round.

### 5. Conditionals for Game Logic
- Implemented logic to compare follower counts and determine the winner.
- Handled cases where both accounts have equal followers.

---

## Project: Higher or Lower Game

### Key Features

1. **Randomized Comparisons**
   - The game selects two random accounts from a dataset for comparison.
   - Ensures the same account is not selected twice in a row.

2. **Follower Count Comparison**
   - Players guess which account has more followers.
   - If the player's guess is correct, the score increases, and the game continues.

3. **Input Validation**
   - Ensures the user enters only `"A"` or `"B"`, prompting again if invalid input is detected.

4. **Score Tracking**
   - Keeps track of the player's correct guesses and displays the current score after each round.

5. **Game Over Condition**
   - The game ends when the player makes an incorrect guess.
   - Displays the final score before exiting.

---

## Key Learnings

1. **Function-Based Design**
   - Encapsulated game logic in functions for clarity and reusability.
   - Reduced redundancy by reusing `format_account()` and `check_answer()` functions.

2. **User Experience Enhancements**
   - Provided dynamic feedback with success and failure messages.
   - Used ASCII art (`logo`, `vs`) to improve visual appeal.

3. **Handling Edge Cases**
   - Managed scenarios where two accounts have equal followers.
   - Ensured accounts do not repeat in consecutive rounds.

4. **Loop Control for Seamless Game Flow**
   - Utilized a `while` loop to keep the game running until an incorrect guess.
   - Reset `account_b` dynamically for each new round.

---

## Possible Improvements

1. **Leaderboard System**
   - Store high scores using a file or database for long-term tracking.

2. **Additional Data Sources**
   - Expand the dataset beyond social media accounts to include other categories.

3. **Hint System**
   - Provide hints such as "Follower count difference is small" for a better gameplay experience.

4. **Graphical User Interface (GUI)**
   - Convert the game into a GUI-based version using `tkinter` or `PyGame`.

5. **Multiplayer Mode**
   - Allow two players to compete by taking turns guessing.

---

## Summary

The **Higher or Lower Game** is an engaging project that reinforces **functions, loops, conditionals, and user input handling**. It provides hands-on experience in building an interactive game while implementing key programming concepts. Future improvements can enhance the game with features like leaderboards, multiplayer modes, and graphical interfaces.

---
