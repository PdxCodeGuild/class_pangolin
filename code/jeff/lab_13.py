# labe_13.py
# Rot 13 Cypher
# Jeff Smith

def rot13(my_str):
    eng = "abcdefghijklmnopqrstuvwxyz"
    crypt = ""
    for char in my_str:
        crypt += eng[(eng.find(char)+13)%26]
    return crypt
my_str = input('What word would you like to obfuscate today? ')
print('Your obfuscated word is: '+ rot13(my_str))

