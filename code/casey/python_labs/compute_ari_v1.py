'''
Lab 22: Compute Automated Readability Index - Version 1

Purpose/goal: Compute the ARI for a given body of text loaded in from a file. The automated readability index (ARI) is a formula for computing the U.S. grade level for a given block of text. The general formula to compute the ARI is as follows:

    - open text.txt file / set variable / read - D
    - create ari scale dict - D
    - create function(s) that return:
        - character count - D
        - word count - D
        - sentence count - D
    - create ari computation function - D
    - compare score with ari scale dict - D
    - print out score with corresponding info: grade level, age range - D

'''

# import string
import string

# import math
import math

# define poss_chars as ascii list
poss_chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# create ari scale dict
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

# open text.txt file / read / set contents variable /
with open('gettysburg_address.txt', 'r') as text_file:
    contents = text_file.read()

# create character counting function
def character_count(contents):
    chars = []
    for char in str(contents):
        if char in poss_chars:
            chars.append(char)
    char_count = len(chars)
    return char_count

# create word counting function:
def word_count(contents):
    words = []
    for char in str(contents):
        if char.isalnum() or char.isspace():
            words.append(char)
        else:
            words.append(' ')
    words_list = "".join(words)
    words_list = words_list.split()
    word_count = len(words_list)
    return word_count

def sentence_count(contents):
    sen_count = 0
    end_list = [".", "!", "?"]
    for end in str(contents):
        if end in end_list:
            sen_count += 1
    return sen_count 

# create ari function
def compute_ari(contents):
    a = character_count(contents) / word_count(contents)
    b = word_count(contents) / sentence_count(contents) 
    c = a * 4.17
    d = b * 0.5
    ari = c + d - 21.43
    ari = math.ceil(ari)
    if ari >= 14:
        ari = 14
    return ari

line = "-" * 70

# compare ari score with ari scale dict
for i in ari_scale:
    if i == compute_ari(contents):
        grade = ari_scale[i]['grade_level']
        years = ari_scale[i]['ages']
        print(f"\n{line}\nThe ARI for gettysburg_address.txt is {compute_ari(contents)}\nThis corresponds to a {grade} Grade level of difficulty\nthat is suitable for an average person {years} years old.\n{line}\n")