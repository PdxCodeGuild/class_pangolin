# 22_ari.py
'''
1. open /read file
2. get # characters
3. get # words
4. get # sentences
5. plug #'s into 4.71(characters/words)+0.5(words/sentences)-21.43 = score
'''
import string
import math
text_file_name = "gettysburg.txt"
###opens the file and reads it, encoding for clarity
with open('gettysburg.txt', 'r', encoding='utf-8') as gettysburg:
    contents = gettysburg.read()
contents = contents.replace(' — ',", ")
# print(contents)
### get number of words by splitting contents of gettysburg into a list
# for letter in contents:
#     if contents == ('— '):
#         contents.replace( '')

words = contents.split()
num_words = len(words)
# print(num_words)
### get number of characters for each word in words list
num_characters = 0
for word in words:
    num_characters += len(word)
# print(num_characters)
### get number of sentences by counting punctuation
num_sentences = 0
punctuation = ['.','?', '!']
for punct in contents:
    if punct in punctuation:
        num_sentences += 1
# print(num_sentences)  
### calculate score with float #, change score to int to cut off decimals, add 1 to round up(all decimals rounded up per instructions)
score = float(4.71)*(num_characters/num_words) + float(0.5)*(num_words/num_sentences) - float(21.43)
score = int(score)
round_score = score + 1
# print(score)
#### provided dictionary
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
print(f"The ARI for {text_file_name} is {round_score}")
print(f"The suitable age range for {text_file_name} {ari_scale[round_score]['ages']}")
print(f"The suitable grade level for {text_file_name} {ari_scale[round_score]['grade_level']}")
# print(contents)




