'''
ROT 13 lab
written by Rhornberger
last updated oct 28 2019
'''
# create a function to Rotate a word 13 spots 
def rot(a):
    a = user_input
    letter = 'abcdefghijklmnopqrstuvwxyz'
    output = ''
    b = input('would you like to pick the number of rotation?: ').lower()
    if b == 'yes':
        c = int(input('What rotation would you like to use?: '))
        for char in a:
            output += letter[(a.find(char)+c)%26]
        return output
    else:
        for char in a:
            output += letter[(a.find(char)+13)%26]
        return output
# take user input and return the answers
user_input = input('What word would you like to obscure?: ').lower()
print(rot(user_input))
