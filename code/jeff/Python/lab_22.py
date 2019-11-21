# lab_22.py
# Compute Automated Readability Index
# Jeff Smith
import math
from collections import Counter 

getty_scale = {
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

with open('getty.txt', "r") as getty_file: 
    getty = getty_file.read() 
    getty = getty.replace("\n", "").replace(",", " ").replace("—", " ").replace("?", ".").replace("!", ".").replace("\r", "")
    getty = " ".join(getty.split())

sent = (len(getty.split('.')))
word = (len(getty.strip('.').split(' ')))
getty = " ".join(getty.split())
getty = getty.replace(" ", "")
char = (len(getty))

score = (4.71 * (char/word)+(.5 * (word/sent) - 21.43))
score = math.ceil(score)
print(f"The ARI for gettysburg-address.txt is {score}. This corresponds to a {getty_scale[score]['grade_level']} level of difficulty that is suitable for an average person {getty_scale[score]['ages']} old.")