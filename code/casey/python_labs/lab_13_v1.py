'''
Lab 13: ROT Cipher - Version 1

Purpose/goal: Write a program that prompts the user for a string, and encodes it with ROT13. 

    - For each character: 
        - Find the corresponding character - D
        - Add it to an output string. - D
        
Notice that there are 26 letters in the English language, so encryption is the same as decryption.

Index	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25
English	a	b	c	d	e	f	g	h	i	j	k	l	m	n	o	p	q	r	s	t	u	v	w	x	y	z
ROT+13	n	o	p	q	r	s	t	u	v	w	x	y	z	a	b	c	d	e	f

'''

# defines rot13 function
def rot13(user_input):
    # defines lets - sting of possible letters
    lets = "abcdefghijklmnopqrstuvwxyz"
    # sets empty output string
    output = ""
    # for loop interates over user_input
    for char in user_input:
        # performs rot13 cipher 
        output += lets[(lets.find(char)+13)%26]
    return output

# request word user would like to encode
user_input = input("Please enter a word to encode: ").lower()

# calls rot13 function, defined as output
output = rot13(user_input)

# returns user's word, encoded
print(f"Your word, encoded: {output}\n")


