# Function to find the highest bidder
def find_highest_bidder(bidding_record):
    max_bid = 0  # Initialize the maximum bid to zero
    max_bidder = ""  # Initialize the highest bidder's name as an empty string

    # Iterate through the bids dictionary to find the highest bid
    for bidder in bids:
        bid_amount = bids[bidder]  # Get the bid amount for the current bidder
        if bid_amount > max_bid:  # Check if the current bid is greater than the maximum bid
            max_bid = bid_amount  # Update the maximum bid
            max_bidder = bidder  # Update the highest bidder
    # Print the winner's name and bid amount
    print(f"The winner is {max_bidder} with a bid of ${max_bid}")

# Initialize an empty dictionary to store the bids
bids = {}
# Variable to control whether the bidding should continue
continue_bidding = True

# Loop to allow multiple bidders to participate
while continue_bidding:
    # Ask the user for their name
    name = input("What is your name? \n")
    # Ask the user for their bid amount and convert it to an integer
    bid = int(input("Enter your bid amount: $"))
    # Save the user's name and bid into the dictionary
    bids[name] = bid

    # Ask if there are more bidders
    should_continue = input("Are there any other bidders? Type 'yes' or 'no': \n").lower()
    if should_continue == "yes":
        # Clear the screen for the next bidder (simulate screen clearing with blank lines)
        print("\n" * 20)
    elif should_continue == "no":
        # If no more bidders, end the loop and find the highest bidder
        continue_bidding = False
        find_highest_bidder(bids)
    else:
        # Handle invalid responses
        print("Invalid response. Please type 'yes' or 'no'.")
