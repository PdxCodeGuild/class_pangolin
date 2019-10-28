'''
Write a program that prompts the user for a character, and encodes it with ROT13. Notice that there are 26 letters in the English language, so encryption is the same as decryption.
Version 2 asks that the user be able to specify the value of the ROT.
'''
import string


def numReturn(user_number):
    index_of_letter = orig_list.index(user_letter)
    number = index_of_letter % len(orig_list)
    return number


def encode_list(orig_list, user_number):
    if user_number < len(orig_list):
        return orig_list[user_number:] + orig_list[:user_number]


orig_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
             "v",
             "w", "x", "y", "z"]

print("This will encode a letter in Rotate format.")

# Asks the user for a lower case letter, looks up that characters position with index. Using the % operator, helps us not to exceed the length of the array and forces it to loop back around. The length of the array is used as a reference so we know when to loop.
# To determine in the custom array (orig_list), its corresponding value.
user_letter = input("Please enter a character: ").lower()
user_number = int(input("How much to rotate by? "))

# numReturn(user_number)
# print(user_number)
index_of_letter = orig_list.index(user_letter)
number = index_of_letter % len(orig_list)
print(index_of_letter)
print(number)
# encode_list(orig_list, user_number)

encoded_list = encode_list(orig_list, user_number)
print(encoded_list)

number2 = len(encoded_list) % index_of_letter
print(number2)
index_of_letter2 = encoded_list.index(user_letter)
print(index_of_letter2)

number3 = index_of_letter2 % 26
print(number3)
# numReturn(user_number)
# print(user_number)
encoded_list.reverse()
print(encoded_list)
# encoded_index_of_letter = encoded_list.index(user_letter)
# print(encoded_index_of_letter)
# number = encoded_index_of_letter % len(orig_list)
# print(number)
# Prints the original value the user entered and shows the encoded character.
print(f"The letter \"{user_letter}\" translates to the letter \"{encoded_list[index_of_letter2]}\" on the ROT-13 list.")
