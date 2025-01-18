# Blackjack Game

## Project Overview
This project is a Python implementation of the classic card game Blackjack. The game is designed to simulate a player-versus-computer experience, with the computer acting as the dealer. It follows the traditional rules of Blackjack, with a few assumptions to simplify the gameplay.

---

## Assumptions and Rules
1. **Deck of Cards**:
   - The deck is unlimited in size.
   - No jokers are included.
   - The cards are represented as: `[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]`, where 11 represents an Ace.
   - All cards have an equal probability of being drawn.
   - Cards are not removed from the deck after being drawn.

2. **Card Values**:
   - Jack, Queen, and King count as 10.
   - Ace can count as either 1 or 11, depending on which is more favorable.

3. **Computer Logic**:
   - The dealer (computer) will draw cards until their score is 17 or higher.

4. **Win Conditions**:
   - Player wins if their score is higher than the dealer’s without exceeding 21.
   - Player loses if their score exceeds 21 (Bust).
   - A draw occurs if both the player and dealer have the same score.

---

## Gameplay Flow
1. **Game Initialization**:
   - The player is prompted to start a game.
   - Two cards are dealt to both the player and the dealer.
   - The player’s cards and total score are displayed.
   - Only the dealer’s first card is shown initially.

2. **Player Actions**:
   - The player can choose to draw another card (Hit) or pass (Stand).
   - If the player’s score exceeds 21, they lose immediately.

3. **Dealer Actions**:
   - The dealer automatically draws cards until their score is 17 or higher.

4. **Determine the Winner**:
   - Compare the player’s and dealer’s scores to determine the outcome.

---

## Features
- **Randomized Card Dealing**: Cards are drawn randomly using Python’s `random` module.
- **Dynamic Scoring**: Handles Ace values dynamically as 1 or 11 based on the current score.
- **User Interaction**: Prompts for user input to decide whether to hit or stand.
- **Dealer Logic**: Implements dealer rules for drawing cards.

---

## Areas of Improvement
1. **Edge Case Management**:
   - Handle scenarios with multiple Aces.
2. **Code Optimization**:
   - Refactor to reduce redundancy and improve readability.
3. **Advanced Features**:
   - Add betting mechanics.
   - Include multiple rounds with cumulative scoring.

---

## How to Run
1. Install Python 3.x.
2. Copy the code into a `.py` file.
3. Run the script in a terminal or an IDE.
4. Follow the on-screen prompts to play the game.

---

## Example Output
```
Welcome to BlackJack!
Do you want to play a game of BlackJack? Type 'y' or 'n': y
Your cards: [10, 9], Current Score: 19
Computer's first card: 7
Type 'y' to get another card, type 'n' to pass: n
Computer's cards: [7, 10], Computer's Score: 17
You win!
