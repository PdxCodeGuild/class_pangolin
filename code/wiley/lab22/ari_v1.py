#ARI grading .10/31/2019 by Wiley Rummel
import string
import os
file_name = 'gettysburg.txt'
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name), 'r') as speech:
    contents = speech.read()

def character_counting(contents):
    '''This function is built to give you a count of ascii letters in a given string 
    and return the number of letters only. '''
    character_list = [] 
    character_num = 0
    for i in contents: 
        if i not in string.ascii_letters:
            contents.replace(i,'')
        if i in string.whitespace:
            contents.replace(i, '')
    for i in contents:
        character_list.append(i)
        for i in character_list: 
            if i not in string.ascii_letters:
                character_list.remove(i)

    character_num += len(character_list)
    return character_num
ari_character_num = character_counting(contents)

def word_counting(contents):
    '''This function returns the number of words in a given string'''
    word_count = 0
    for i in contents:
        if i == '-':
            contents.replace('-', ' ')
    for i in range(len(contents)):
        if contents[i] == ' ' or contents[i] == '\n' or contents[i] == '\t':
            word_count += 1
        
    return word_count

ari_word_count = word_counting(contents)

def sentence_counting(contents):
    '''This function returns the number of sentences in a given string.'''
    sentence_count = 0
    wait = 4
    for i in range(len(contents)):
        wait -=1
        if contents[i] in ('.','!','?','...','\n','\t') and wait < 0:
            sentence_count +=1
            wait = 4

            

        
    return sentence_count

ari_sentence_count = sentence_counting(contents)

def ari_formula(x,y,z):
    '''This formula takes in three arguments.  Chacters, Words, and Sentences in that order.  It then returns an ARI with the given data.'''
    ari = (4.71*(x/y))+(.5*(y/z)) -21.43
    ari = round(ari)
    if ari >= 14:
        ari == 14
    return ari

ari = ari_formula(ari_character_num, ari_word_count, ari_sentence_count)

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


def scale_loop_up(ari):
    
    var = ari_scale.get(ari)
    ages = var.get('ages')
    grade_level = var.get('grade_level')
    return ages, grade_level
ages1, grade_level1 = scale_loop_up(ari)

    

    

print(f"{ari_character_num} characters in the speech.")
print(f"{ari_word_count} words in the speech.")
print(f"{ari_sentence_count} sentences in the speech.")
print(f"{ari} is the ARI score of the speech.")
print(f"The ARI for {file_name} is {ari}.\nThis corresponds to a {grade_level1} level of difficulty.\nThat is suitale for an average person {ages1} years old.")


        























