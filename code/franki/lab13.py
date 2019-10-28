cipher = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def rot_13(a):
    cipher_input = list(a)
    cipher_output = []
    ciphertext = ""
    for letter in cipher_input:
        x = cipher.index(letter)
        if x < 13:
            y = cipher[x + shift]
        elif x >= 13:
            y = cipher[x - shift]
        cipher_output.append(y) 
    return ciphertext.join(cipher_output)
print("Welcome to the Caesar Cipher Generator.") 
shift = int(input("Enter the number of steps you would like to shift (1-13). "))   
plaintext = input("Enter the text you would like to encrypt. ").lower()
print(rot_13(plaintext))