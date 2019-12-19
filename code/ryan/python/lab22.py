with open('big_lebowski.txt', 'r') as f:
    contents = f.read()
import string
import math

words = contents.split()
num_words = len(words)
characters = 0
sentences = 0

for word in words:
    characters += len(word)
    if len(word) > 1:
        if word[-2] in string.ascii_letters and word[-1] in [".", "!", "?"]:
            sentences += 1

ari = math.ceil((4.71 * (characters/num_words)) + (.5 * (num_words/sentences) - 21.43))

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

print(f"The ARI for this text is {ari}.  This corresponds to a {ari_scale[ari]['grade_level']} grade level of difficulty, and is suitable for a person {ari_scale[ari]['ages']} years old.")
