import random

from game_data import data
from art import logo, vs


def format_account(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"

def check_answer(user_input, a_followers, b_followers):
    """Take a user's guess and the follower counts and returns if they got it right."""
    if a_followers == b_followers:
        return False
    elif a_followers > b_followers:
        return user_input == "a"
    else:
        return user_input == "b"

def higher_lower():
    print (logo)
    score = 0
    account_b = random.choice(data)

    game_continue = True

    while game_continue:
        account_a = account_b

        while account_a == account_b:
            account_b = random.choice(data)

        print(f"Compare A: {format_account(account_a)}")
        print (vs)
        print(f"Compare B: {format_account(account_b)}")

        user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        while user_guess not in ['a', 'b']:
            user_guess = input("Invalid Input! Please select 'A' or 'B': ").lower()

        a_followers_count = account_a['follower_count']
        b_followers_count = account_b['follower_count']

        is_correct = check_answer(user_guess, a_followers_count, b_followers_count)
        print(is_correct)

        print(logo)
        print('\n'* 40)


        if is_correct:
            score += 1
            print (f"Your are right! Current Score: {score}")
            account_a = account_b
        else:
            game_continue = False
            print (f"Sorry, that's wrong. Final Score: {score}")

higher_lower()