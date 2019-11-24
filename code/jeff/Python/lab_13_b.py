# labe_13.py
# Rot 13 Cypher
# Jeff Smith

def rot(my_str):
    eng = "abcdefghijklmnopqrstuvwxyz"
    crypt = ""
    for char in my_str:
        crypt += eng[(eng.find(char)+ my_rot)%26]
    return crypt
my_str = input('What word would you like to obfuscate today? ')
my_rot = int(input('How may characters would you like to shift your word?' ))
print('Your obfuscated word is: '+ rot(my_str))

