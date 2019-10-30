# Shawn Stolsig
# PDX Code Guild 
# Assignment: Practice 3 - Dictionaries
# Date: 10/30/2019

import string

def combine(a, b):
    # my_list = []
    # for i in range(len(a)):
    #     my_list.append((a[i],b[i]))
    # return dict(my_list)
    my_dict = {}
    for i in range(len(a)):
        my_dict[a[i]] = b[i]
    return my_dict

# fruits = ['apple', 'banana', 'pear']
# prices = [1.2, 3.3, 2.1]
# print(combine(fruits, prices)) # -> {'apple':1.2, 'banana':3.3, 'pear':2.1}

def average(d):
    sum = 0
    for key in d:
        sum += d[key]
    return sum / len(d.items())

combined = {'apple':1.2, 'banana':3.3, 'pear':2.1}
print(average(combined)) # -> 2.2

def unify(d):
    new_dict = {}
    
    for letter in string.ascii_letters:
        sum = 0
        counter = 0
        for key in d:
            print(f'key[0] is {key[0]} and letter is {letter}')
            if key[0] == letter:
                sum += d[key]
                counter += 1
        if counter >= 1:
            new_dict[letter] = sum/counter

    return new_dict

d = {'a1':5, 'a2':2, 'a3':3, 'b1':10, 'b2':1, 'b3':1, 'c1':4, 'c2':5, 'c3':6}
print(unify(d)) #-> {'a':3, 'b':4, 'c':5}