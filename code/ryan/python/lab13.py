import string
english = list(string.ascii_lowercase)
rot_13 = english[13:] + english[:13]
encoded = []
convert = list(input("Enter any word or phrase to convert to ROT13:  "))

for letter in convert:
    encoded.append(english.index(letter))
encoded = [rot_13[letter] for letter in encoded]
output = "".join(encoded)

print(output)
