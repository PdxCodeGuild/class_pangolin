'''
lab 22 ARI 
written by Rhornberger
last updated oct 31 2019
'''
import string

# open the file and set to close after the program is done.
with open('gettysburg.txt', 'r') as gettysburg_file:
    contents = gettysburg_file.read()

# manipulate the data  
new_content = contents.split()
new_content2 = [word.strip(string.punctuation) and word.strip(string.digits) for word in contents.split()]
new_content1 = contents.split('.')
new_content3 = [sentence.strip(string.punctuation) and sentence.strip(string.digits)for sentence in new_content1]
new_content_sentences = []
for s in new_content3:
    if s not in ('', '\n', '\t', ' '):
        new_content_sentences.append(s)
new_content_words = []
for w in new_content2:
    if w not in ('', '\n', '\t', ' '):
        new_content_words.append(w)
new_content_char =[]
for i in contents:
    if i not in ('', '\n', '\t', ' '):
        new_content_char.append(i) 

# dictionary for the ARI
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

# Do the math 
a = (len(new_content_char) / len(new_content_words))
b = (len(new_content_words) / len(new_content_sentences))
ari = int(4.71 * a + 0.5 * b - 21.43)

# consult the dictionary
grade_level = ari_scale[ari]['grade_level']
age_level = ari_scale[ari]['ages']

# Return the information to the user
print(f'The ARI for the Gettysburg Address is {ari}, this corresponds to {grade_level} level of difficulty, and the suggested age range is {age_level}.')
