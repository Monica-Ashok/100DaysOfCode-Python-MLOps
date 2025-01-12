# Day 07 - Hangman Game

## Key Concepts Covered:
- **Flow Chart Design:** Breaking down a complex problem into smaller steps for easier implementation.
- **Random Module:** Selecting random words from a predefined list for the game.
- **ASCII Art:** Enhancing the game experience with visual representations of the hangman stages.
- **String Manipulation:** Replacing blanks with correct guesses.
- **Game Logic:** Tracking player lives and determining win/lose conditions.

---

## Project 07 - Hangman Game

### Project Overview:
For today's project, I built a **Hangman Game** in Python. This game randomly selects a word, and the player must guess it one letter at a time while avoiding incorrect guesses that deplete their lives. The game includes:

1. **Random Word Selection:** Using the `random` module to pick words from a predefined list.
2. **ASCII Art Integration:** Displaying visual stages of the hangman for each incorrect guess.
3. **Dynamic Word Display:** Replacing blanks with correctly guessed letters.
4. **Player Feedback:** Informing the player about lives left, repeated guesses, and incorrect guesses.

---

### Features and Improvements:

1. **ASCII Art for Hangman Stages:**
   - The game uses ASCII art from `hangman_art.py` to visually represent the hangman progress.

   ```python
   stages = [
       '''
          -----
          |   |
          O   |
         /|\  |
         / \  |
             -----
       ''',
       # (Other stages follow...)
   ]
   ```

2. **Random Word Selection:**
   - The `random.choice()` function is used to pick a word from the `word_list` in `hangman_words.py`.

3. **Tracking Player Lives:**
   - The player starts with 6 lives, which decrease with each incorrect guess. The game ends when lives reach 0.

4. **Dynamic Word Placeholder:**
   - The word to guess is displayed as underscores (`_`) that are replaced with correctly guessed letters.

5. **Handling Repeated Guesses:**
   - If the player guesses a letter they already guessed, the game informs them without deducting lives.

6. **Feedback for Incorrect Guesses:**
   - The game informs the player about incorrect guesses and deducts a life.

7. **Final Message:**
   - At the end of the game, the player is informed whether they won or lost, along with the correct word.

---

### Edge Cases Handled:
- **Repeated Guesses:**
  - The game prevents lives from being deducted for repeated guesses.
- **Invalid Inputs:**
  - Currently, the game assumes valid single-letter inputs. Future versions could include checks for invalid inputs (e.g., numbers or special characters).
- **Empty Input:**
  - The game does not explicitly handle empty inputs yet.

---

### Future Enhancements:
1. **Hint System:**
   - Deduct a life to reveal a random letter in the word.
2. **Difficulty Levels:**
   - Allow the player to choose difficulty levels with varying word lengths or number of lives.
3. **Scoring System:**
   - Implement a scoring system for multiple rounds.
4. **Improved Input Validation:**
   - Add checks for invalid inputs like numbers, special characters, or empty guesses.