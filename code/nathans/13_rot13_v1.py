# encode_rot.py
'''
To do list: 1.Change input to accept string
            2. Clean up and annotate.
            3. git 
'''



import string
import math
letter_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
user_letter = input("Enter a character to encrypt: ").lower()
# user_rot_num = input("Enter rotation number: ")
number_1 = string.ascii_lowercase.index(user_letter) 
number_1 = int(number_1)
rot_number = number_1 + 13
# user_letter_index = int(number_1)

if number_1 <= 12:
    # print(rot_number)
    print(letter_list[rot_number])
elif number_1 > 12:
    newest_num =(number_1 + rot_number)%25
    # print(newest_num)
    print(letter_list[rot_number])
# letter_list = []
#letter_list.append(string.ascii_lowercase)

# print(letter_list[rot_number])



    
   
    

# rot_list = ['n', 'o','p','q','r', 's', 't', 'u', 'v', 'w','x', 'y','z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'].index()

# number_2 = int(rot_list)

# print(f"{user_letter_index}")

# print(f"You entered: {number_1}")
