'''Write a program that prompts the user for a character, and encodes it with ROT13. Notice that there are 26 letters in the English language, so encryption is the same as decryption.'''

def numReturn():
    number = string.ascii_lowercase.index(user_letter) + 1
    number = number % len(rot13_list)
    return number

import string

# A custom list/array of characters used for encoding.
rot13_list = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h",
              "i", "j", "k", "l", "m"]

print("This will encode a letter in ROT-13 format")

# Asks the user for a lower case letter, looks up that characters position with index. Using the % operator, helps us not to exceed the length of the array and forces it to loop back around. The length of the array is used as a reference so we know when to loop.
# To determine in the custom array (rot13_list), its corresponding value.
user_letter = input("Please enter a character: ").lower()

number = numReturn()

# Prints the original value the user entered and shows the encoded character.
print(f"The letter \"{user_letter}\" translates to the letter \"{rot13_list[number - 1]}\" on the ROT-13 list.")
