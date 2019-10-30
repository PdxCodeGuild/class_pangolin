# Write a function that takes a string, and returns a list of strings, each missing a different character.

userInput = "kitten"

word_list = []

len_userInput = len(userInput)
# print(len_userInput)
lst_userInput = list(userInput)
# print(lst_userInput)
x = 0
for i in lst_userInput:
    # print(i)
    word_list.append(i)
    # word_list.pop(i)
    print(word_list)
