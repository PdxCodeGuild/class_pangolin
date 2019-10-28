#Bieschke Lab 13: ROT Cipher v2 
#I'd tell you what this program does, but then I'd have to kill you

rot_13 = "abcdefghijklmnopqrstuvwxyz"

def doom():
    k = int(input("What number of rotation would you like your cipher? Negatives decrypt."))
    code = []
    new_letters = []
    transform = []
    for letter in letters:
        codes = rot_13.find(letter) + k
        codes1 = int(codes)%26
        code.append(codes1)
    print(f"The secret code is {code}")

    for nums in code:
        new_letter = nums
        new_letter1 = (new_letter)%26
        new_letters.append(new_letter1)
        transform.append(rot_13[new_letter1])
    print(f"The coded phrase is {transform}")

lions = True
while lions == True:
    print("Hello! We're on a secret mission!\n")
    message = input("What's the message I need to encrypt? Or press enter to quit.")

    if message == '':
        print("Sayonara!")
        quit()
    else:
        message.lower()
        letters = message.replace(" ", "")
        doom()