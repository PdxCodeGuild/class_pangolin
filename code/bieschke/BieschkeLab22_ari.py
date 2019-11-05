#BieschkeLab 22: automated readability index

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

def ari(letters_param, word_param, sentences_param):
    return (4.71*(letters_param/word_param) + .5*(word_param/len(sentences_param)) - 21.43)//1 + 1

print("Hello! This script calculates the ARI of a text loaded from a file.")
#y = input("What file would you like to test? I recommend Demons.txt\n>")
y = 'gettysburg.txt'

with open(y) as sampled_file:
    word = 0
    letters = 0
    #sentences = sampled_file.read().replace(' ', '')
    sentences = sampled_file.read().split('.')

    for line in sentences:
        #sampled_file.read().
        print(line.strip(' '))
        letters += len(line.replace(' ', '').replace('\n', ''))

        for words in line.split():
            word +=1
            
        num_words = len(words)
        print(f"{word} words counted in this file")
        print(f"{letters} letters counted in this file")

    print(f"{len(sentences)} sentences in this file\n")

# sentences.remove('')
x = ari(letters, word, sentences)
if x > 14:
    x = 14 
#print(x)
#print(ari_scale.get(ari()))
print(f"The ARI for {sampled_file.name} is {x}")
print(f"This corresponds to a {ari_scale[int(x)]['grade_level']}")
print(f"This is suitable for an average person {ari_scale[int(x)]['ages']} years old")
