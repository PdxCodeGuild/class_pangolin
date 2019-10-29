# Anagram checker
user_input_1 = sorted(input("Enter the first word  > ").lower().replace(' ', ''))
user_input_2 = sorted(input("Enter the second word  > ").lower().replace(' ', ''))

print(user_input_1)
if user_input_1 == user_input_2:
    print("Anagram!")

