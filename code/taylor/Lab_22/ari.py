# Taylor Rebbe
# PDX Code Guild
# Lab_22 
# 10/31/2019

# Import math library
import math
import string

doc1 = './code/taylor/Lab_22/wrds_doc.txt'

# ARI dictionary, free of charge
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
# Find number of sentences
def get_snt(d):
    with open(d) as f:
        num_snt = f.read().count('.')
        return num_snt

# Find number of words
def get_wrd(d):
    with open(d) as f:
        for line in f:
            num_wrd = len(line.split())
            return num_wrd

# Find number of letters
def get_chr(d):
    with open(d) as f:
        num_chr = len(f.read().translate(str.maketrans('', '', string.punctuation)).replace(' ',''))
        return num_chr

# Ages for user output
def get_ags(a):
    for k, v in a.items():
        if k == ari:
            return v['ages']

# Grade for user output
def get_grd(a):
    for k, v in a.items():
        if k == ari:
            return v['grade_level']

# ARI formula, spared at no expense
ari = math.floor((4.71 * (get_chr(doc1) / get_wrd(doc1)) + 0.5 * (get_wrd(doc1) / get_snt(doc1)) - 21.43))

# For all those PHd's
if ari >= 14:
    ari = 14
    
# User output     
print(f"\nThe ARI for [ {doc1} ] is: > {ari} ")
print(f"\nThis corresponds to a {get_grd(ari_scale)} Grade level of difficulty")
print(f"That is suitable for an average person {get_ags(ari_scale)} years old.")
