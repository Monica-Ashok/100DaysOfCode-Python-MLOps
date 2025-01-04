# Day 04 - Randomisation and Python Lists

## Key Concepts Covered:

- **Random Module**: Used to generate a random choice for the computer between rock, paper, and scissors.
- **Lists**: Used to store the string representations of rock, paper, and scissors, making the code more modular and readable.
- **Index Errors**: Handling user input and ensuring that only valid options are selected.
- **Nested Lists**: While not explicitly used in this version, the game could be expanded to incorporate more complex data structures like nested lists for advanced features.

---

## Project 04 - Rock, Paper and Scissors

## Overview

This is a simple implementation of the classic **Rock, Paper, Scissors** game in Python. The game allows the user to choose between rock, paper, or scissors, and the computer randomly selects one of the three options. The outcome of the game is determined based on the following rules:

- **Rock** beats **Scissors**
- **Scissors** beats **Paper**
- **Paper** beats **Rock**
- If both the player and computer choose the same option, it's a **draw**.

---

## Features

- **User Input Validation**: Ensures the player selects a valid option (0, 1, or 2).
- **Random Computer Choice**: The computer's selection is random, making each game unpredictable.
- **Clear Outcome Display**: The result of the game is clearly printed, showing both the player's and the computer's choices.

---


## How the Game Works

1. The user is prompted to choose between rock, paper, or scissors by typing `0`, `1`, or `2`, respectively.
2. The program then randomly generates a choice for the computer.
3. The game compares the user’s choice with the computer’s choice to determine the winner.
4. The result (win, loss, or draw) is displayed accordingly.

---

### Invalid Selection Handling

If the user enters a number outside the valid range (i.e., not 0, 1, or 2), the game will display an **"Invalid number, you lose!"** message and end the game. This ensures that only valid choices are accepted.
