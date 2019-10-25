# Shawn Stolsig
# PDX Code Guild 
# Assignment: Practice 2 - Strings
# Date: 10/25/2019

import string

def double_letters(word):
    newstring = ''
    for letter in word:
        newstring += letter*2
    return newstring

# print(double_letters('hello')) # hheelllloo

def list_missing_letter(word):
    return_list = []

    for i in range(0,len(word)):
        append_me = ''
        for letter in word:
            if letter == word[i]:
                pass
            else:
                append_me += letter
        return_list.append(append_me)
        
    return return_list

# print(list_missing_letter('kitten'))

def latest_letter(word):
    word_list = list(word)
    word_list.sort()
    return word_list[-1]

# print(latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis'))

def how_many_hi(word):
    counter = 0
    for i in range(0,len(word)-1):
        if word[i]=='h' and word[i+1]=='i':
            counter += 1
    return counter

# print(how_many_hi('hihisdfwerhihii'))

def count_letter(letter,word):
    counter = 0
    for let in word:
        if let == letter:
            counter += 1
    return counter

# print(count_letter('i', 'antidisestablishmentterianism')) # 5
# print(count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis')) #2

def lower_case(input):
    output = input.strip()
    output = output.lower()
    return output

print(lower_case("SUPER!")) # super!
print(lower_case("        NANNANANANA BATMAN        ")) # 'nannananana batman'