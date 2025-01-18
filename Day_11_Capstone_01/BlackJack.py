import random

# Define the deck of cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def calculate_score(hand):
    """Calculate the score of a given hand, adjusting for Aces."""
    score = sum(hand)
    if 11 in hand and score > 21:
        hand.remove(11)
        hand.append(1)
        score = sum(hand)
    return score

def deal_card():
    """Return a random card from the deck."""
    return random.choice(cards)

def evaluate_winner(player_score, dealer_score):
    """Determine the winner based on scores."""
    if player_score > 21:
        return "Bust! You lose!"
    elif dealer_score > 21:
        return "Dealer busts! You win!"
    elif player_score == dealer_score:
        return "It's a draw!"
    elif player_score > dealer_score:
        return "You win!"
    else:
        return "You lose!"

def blackjack():
    print("Welcome to Blackjack!")

    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
        player_hand = [deal_card(), deal_card()]
        dealer_hand = [deal_card(), deal_card()]

        game_over = False

        while not game_over:
            player_score = calculate_score(player_hand)
            dealer_score = calculate_score(dealer_hand)
            print(f"Your cards: {player_hand}, current score: {player_score}")
            print(f"Dealer's first card: {dealer_hand[0]}")

            if player_score == 21:
                print("Blackjack! You win!")
                game_over = True
            elif player_score > 21:
                print("Bust! You lose!")
                game_over = True
            else:
                if input("Type 'y' to get another card, type 'n' to pass: ").lower() == 'y':
                    player_hand.append(deal_card())
                else:
                    game_over = True

        # Dealer's turn
        while dealer_score < 17:
            dealer_hand.append(deal_card())
            dealer_score = calculate_score(dealer_hand)

        print(f"Your final hand: {player_hand}, final score: {player_score}")
        print(f"Dealer's final hand: {dealer_hand}, final score: {dealer_score}")
        print(evaluate_winner(player_score, dealer_score))

    print("Thanks for playing!")

# Run the game
blackjack()
