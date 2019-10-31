import math
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
def count_sentences(x):
    periods = x.count('.')
    questions = x.count('?')
    exclamations = x.count('!')
    sentence_count = periods + questions + exclamations
    return sentence_count

def list_words(x):
    words = x.split()
    return(words)

def count_characters(x):
    punctuations = ''',/?!)(-._'":;'''
    no_punct = []
    characters = ""
    characters = characters.join(x)
    for char in characters:
        if char not in punctuations:
            no_punct.append(char)
    character_count = len(no_punct)
    return character_count

    
       
with open('boat_of_ra.txt', 'r') as file:
    poem = file.read()
    words = list_words(poem)
    word_count = len(words)
    character_count = count_characters(words)
    sentence_count = count_sentences(poem)
    ari = (4.71*(character_count / word_count)) + (0.5*(word_count / sentence_count)) - 21.43
    ari = math.ceil(ari)
    print(sentence_count)
    print(word_count)
    print(character_count)
    print(f"The Automated Readability Index of this text is: {ari}.")
    print(f"This corresponds to {ari_scale[ari]['grade_level']} reading level.")
    print(f"It is suitable for ages {ari_scale[ari]['ages']}.")
