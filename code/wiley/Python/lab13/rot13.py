#Write a program that prompts the user for a string, and encodes it with ROT13. 
#For each character, find the corresponding character, add it to an output string.
#Notice that there are 26 letters in the English language, so encryption is the same as decryption.

#k = key (the rotations to get the letter)
#p = input letter (to be encrypted)
#c = the encrypted letter

#basic encryption formula is c = k+p
#thorough encryption formula is c = (p + k)%26
#thorough decryption formula is c = (p - k)%26
#the modulo wraps the letters back around to find the letter if the p+k value is greater than 26 (length of the alphabet)

#build list of the alphabet


#define encryption function
#take input string
#break user string into a list
#apply formula to each item in the list
#turn the list back into a string

import string

def encryption():
    alphabet_dict = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
    alphabet_list = list(alphabet_dict.keys())

    #print(len(alphabet))
    numerical_list = []
    encrypted_list = []
    encrypted_message_list = []
    user_message = input("What do you want to be encrypted?\n").lower()
    message_list = [x for x in user_message]
    #print(message_list)
    k = int(input("How many encryption rotations would you like? Use negative to decrypt an excrypted message.\n"))
    #makes a list of the values of user input
    for i in message_list:
        index = alphabet_dict.get(i)
        #print(index)
        numerical_list.append(index)
        #print(numerical_list)
    
    #rotates + 13 to the encrypted value, then appends that value into a new list which uses that value as an index for the alphabet_list
    #returning the encrypted message as a list
    for i in numerical_list:
        encrypted_value = (i + k)%25
        encrypted_list.append(encrypted_value)
        encrypted_message_list.append(alphabet_list[encrypted_value])
        #print(encrypted_value)
        
    #print(encrypted_list)
    #print(encrypted_message_list)
    encrypted_message_str = ''
    for i in encrypted_message_list:
        encrypted_message_str += str(i)
    #print(encrypted_message_str)
    print(encrypted_message_str)
    return encrypted_message_str
    

encryption()