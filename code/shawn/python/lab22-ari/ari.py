# Shawn Stolsig
# PDX Code Guild 
# Assignment: Lab 19 - Automated Reliability Index
# Date: 10/31/2019

import string
import math

# provided ARI scale
ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

# main loop
while True: 
    # get input for opening file
    print("Files currently in this folder are day_of_infamy.txt trump.txt and gettysburg_address.txt")
    user_file_name = input("Please input filename, or press enter to quit: ")
    # user_file_name = 'gettysburg_address.txt'

    # quit if no input
    if not user_file_name:
        break

    # open file, store in a string
    with open(user_file_name, 'r') as f:
        file_string = f.read()                

    # to get number of sentences, split on '.'
    num_sentences = file_string.count('.') + file_string.count('!') + file_string.count('?')

    # to get number of words, count spaces.  strip trailing/leading white space and all newlines first
    file_string = file_string.strip()
    file_string = file_string.replace('\n', ' ')

    # count number of spaces to get number of words
    num_words = file_string.count(' ')

    # to get number of characters, iterate through and count only letters
    num_char = 0
    for letter in file_string:
        if letter in string.ascii_letters:
            num_char += 1

    # print out counts
    print(f'there are {num_sentences} sentences')
    print(f'there are {num_words} words')
    print(f'there are {num_char} characters')
    
    # calculate ARI score
    ari_score = math.ceil(   (4.71  *  (num_char/num_words)  ) + (0.5*   (num_words/num_sentences)   ) - 21.43)

    # max score is 14 for college
    if ari_score > 14:
        ari_score = 14

    # print ARI message
    print('--------------------------------------------------------')
    print(f'The ARI score for {user_file_name} is {ari_score}')
    print(f"This corresponds to a {ari_scale[ari_score]['grade_level']} level of difficulty")
    print(f"that is suitable for an average person {ari_scale[ari_score]['ages']} years old")
    print('--------------------------------------------------------')

print('quitting')