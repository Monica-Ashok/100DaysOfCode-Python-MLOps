import random


# Function to check the guess
def evaluate_winner(computer_input, user_input):
    """Determine if the guess is correct or not."""
    if computer_input > user_input:
        return "Too Low."
    elif computer_input < user_input:
        return "Too High."
    else:
        return f"You got it! The number was {user_input}"

def number_guess():
    print("🎲 Welcome to the Number Guessing Game 🎲\n"
          "I'm thinking of a number between 1 to 100.")

    # Choose difficulty
    while True:
        difficulty = input("Choose a difficulty: Type 'easy' or 'hard': ").lower()
        if difficulty == 'hard':
            attempts = 5
            break
        elif difficulty == 'easy':
            attempts = 10
            break
        else:
            print("Invalid Input. Choose 'easy' or 'hard'.")

    # Generate random number
    computer_input = random.randint(1, 100)
    print(computer_input)  # For Testing, remove later

    # Game Loop
    while attempts > 0:
        try:
            user_input = int(input("Make a guess: "))
        except ValueError:
            print("❌ Please enter a valid number.")
            continue # Restart loop if input is not a number

        result = evaluate_winner(computer_input, user_input)

        if "You got it!" in result:
            print(result)
            break

        attempts -= 1
        print(f"{result} You have {attempts} attempts remaining.")

        if attempts == 0:
            print("You've run out of guesses. Refresh the game to play again!")

number_guess()