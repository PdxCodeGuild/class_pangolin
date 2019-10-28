import string
english = list(string.ascii_lowercase)
encoded = []
convert = list(input("Enter any word or phrase to convert:  "))
shift = int(input("Set your own encoding parameter.  How many spaces would you like each letter to shift?  "))

for letter in convert:
    encoded.append(english.index(letter))
encoded_letters = [english[num + shift] if num + shift <= 25 else english[(num + shift) % 26] for num in encoded]

output = "".join(encoded_letters)
print(output)
