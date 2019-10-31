# Shawn Stolsig
# PDX Code Guild 
# Assignment: Practice 5 - Comprehensions
# Date: 10/30/2019

import string

def powers_of_two():
    return [2**num for num in range(10)]

# print(powers_of_two())

def first_10_even_num():
    return [num for num in range(20) if num%2 == 0]
# print(first_10_even_num())

def swap_pairs(my_dict):
    return {value: key for key, value in my_dict.items()}
# print(swap_pairs({'a': 1, 'b': 2}))

def get_ascii_alphabet():
    return {letter: ord(letter) for letter in string.ascii_lowercase}
print(get_ascii_alphabet())