#Bieschke Lab 13: ROT Cipher 
#I'd tell you what this program does, but then I'd have to kill you

'''
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h",
    8: "i",
    9: "j",
    10: "k",
    11: "l",
    12: "m",
    13: "n",
    14: "o",
    15: "p",
    16: "q",
    17: "r",
    18: "s",
    19: "t",
    20: "u",
    21: "v",
    22: "w",
    23: "x",
    24: "y",
    25: "z"
    '''

rot_13 = "abcdefghijklmnopqrstuvwxyz"

def doom():
    #letters = letters.split(' ')
    
    k = 13
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