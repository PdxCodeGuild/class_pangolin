
#Write a program that prompts the user for a string- done , and encodes it with ROT13. For each character, find the corresponding character, add it to an output string. Notice that there are 26 letters in the English language, so encryption is the same as decryption.

from string import ascii_lowercase

#def rot_loop ():

user_input = "hello"
# input('What prase would you like to encode? :  ')
# user_input = list(user_input)
# print (user_input)
# for i in range(len(user_input)):
# print(ascii_lowercase.index (user_input)
# # x = ''
# if x in (user_input):
#     print (ascii_lowercase.index (user_input) + 13 % 26)
new = []
for letter in user_input:
    new.append (ascii_lowercase.index(letter))
# print (user_input)
new_list = [x+13 for x in new]

final_list = [x % 26 for x in new_list]

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

final_num= []
for number in final_list:
    final_num.append(ascii_lowercase.index)
print (new)
print (new_list)
print(final_num)
print (final_list)

# print (letters.index(final_list)) 
#ask about this 

    #user_input2 = [new] + 13
   # user_input2 = int(new) % 26
#print (new)
    #print (user_input2)

#print (ascii_lowercase[new])

#print (chr(user_input2 +97))



# new1 = ascii_lowercase (str(new))
# print (new)
 
#rot_loop()

# letters = input(str('What prase would you like to encode? :  '))
# user = letters % 26

# for letter in letters:
#     number = ord(letter)
#     print (number)

