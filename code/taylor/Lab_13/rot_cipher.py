# Taylor Rebbe
# PDX Code Guild
# Lab_13v2
# 10/28/2019

# User inputs, text string and rotation number for encryptin
usr_str1 = list(str(input("Enter some text: > ")).lower())
usr_rot1 = int(input("Enter a rotation (1 - 18): > "))

# Initialized lists for encryption / decryption functions
e_list = []
d_list = []

# Rot encryption function, accomidates spaces 1 - 18 Rot without bugs
def rot_encrypt(lst, rot, el):
    for i in lst:
        b = int(str(ord(i) + rot))
        while b > 122:
            b += -122 + 96
        if b - rot == 32:
            b = 32
        el.append(chr(b))

# Rot decryption function, accomidates spaces 1 - 18 Rot without bugs
def rot_decrypt(lst, rot, dl):
    for i in lst:
        b = int(str(ord(i) - rot))
        while b < 97:
            if b + rot == 32:
                b = 32
                dl.append(chr(b))
                break
            c = 96 - b
            b = 122 - c
        dl.append(chr(b))

# Encryption function call
rot_encrypt(usr_str1, usr_rot1, e_list)

# Returns the encryption list to a string
lst_to_str = ''.join([str(i) for i in e_list]) 
print(lst_to_str)

# User inputs, text string and rotation number for decryption
usr_str2 = list(str(input("Enter some text: > ")).lower())
usr_rot2 = int(input("Enter a rotation (1 - 18): > "))

# Decryption function call
rot_decrypt(usr_str2, usr_rot2, d_list)

# Returns the decryption list to a string
lst_to_str = ''.join([str(i) for i in d_list]) 
print(lst_to_str)

