# Day 8 - Caesar Cipher

## Key Concepts Covered:
- **Functions with Inputs:** Understanding how to pass arguments to functions.
- **Positional vs. Keyword Arguments:** Exploring how to use both in Python functions.
- **String Manipulation:** Modifying strings based on user input.
- **Modulo Operation:** Wrapping around the alphabet using the modulo operator.
- **Looping:** Repeating the process of encoding/decoding until the user decides to stop.

---

## Project Overview:
Today’s project is a **Caesar Cipher** implementation, one of the oldest encryption techniques. The cipher shifts each letter in the alphabet by a specified number of positions. You can either **encode** or **decode** a message using this method.

### How It Works:
1. **User Input:**
   - The program asks whether you want to **encode** or **decode** a message.
   - You then input the message you want to encrypt or decrypt.
   - A shift number is provided to determine how many positions the letters will be shifted.

2. **Encoding and Decoding Logic:**
   - When encoding, each letter is shifted forward in the alphabet by the given shift number.
   - When decoding, the shift is reversed (negative shift), moving the letters backward by the same number.

3. **Handling Non-Alphabet Characters:**
   - The program leaves spaces, punctuation marks, and numbers unchanged.

4. **Loop for Repeated Use:**
   - After encoding/decoding a message, the program asks if you want to try again or exit. The loop continues until the user chooses to stop.

---

## Code Explanation:

### The `caesar()` Function:
This function handles the core logic of the Caesar Cipher. It accepts three parameters:
- `original_text`: The message to be encoded or decoded.
- `shift_amount`: The number of positions to shift each letter.
- `encode_or_decode`: A string that indicates whether to encode or decode the message.

```python
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")
