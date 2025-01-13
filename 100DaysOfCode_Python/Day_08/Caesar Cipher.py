from art import logo  # Import the 'logo' variable from the 'art' module (you'll need to have this module available).
print(logo)  # Print the logo to the screen when the program starts.

# Define the alphabet list to use for encoding/decoding.
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# This function will encode or decode a given text based on the direction and shift amount.
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""  # Initialize an empty string to store the result.

    # If the operation is "decode", reverse the shift by multiplying by -1.
    if encode_or_decode == "decode":
        shift_amount *= -1

    # Loop through each letter in the original text.
    for letter in original_text:
        # If the letter is not in the alphabet (like a space, symbol, or number), add it to the result as is.
        if letter not in alphabet:
            output_text += letter
        else:
            # Find the index of the letter in the alphabet and shift it by the given amount.
            shifted_position = alphabet.index(letter) + shift_amount
            # Use modulo to ensure the position wraps around the alphabet (so it doesn't go out of bounds).
            shifted_position %= len(alphabet)
            # Add the new letter to the output text.
            output_text += alphabet[shifted_position]

    # Print the final result after encoding/decoding.
    print(f"Here is the {encode_or_decode}d result: {output_text}")

# Set a flag to keep the program running until the user decides to stop.
again = True
while again:
    # Ask the user whether they want to encode or decode the message.
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    # Ask the user to input the message they want to encode/decode.
    text = input("Type your message:\n").lower()
    # Ask the user to input the shift number (how many positions to shift each letter).
    shift = int(input("Type the shift number:\n"))

    # Call the caesar function to encode/decode the text.
    caesar(text, shift, direction)

    # Ask the user if they want to repeat the program.
    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    # If the user types 'no', set the flag to False and exit the loop.
    if restart == "no":
        again = False
        print("Goodbye")  # Print a goodbye message when the program ends.
