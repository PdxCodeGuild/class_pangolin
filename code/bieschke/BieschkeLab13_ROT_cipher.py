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
    letters = message.replace(" ", "")
    #letters = letters.split(' ')
    print(type(letters))
    new_letters = ""
    for letter in letters:
        code = rot_13.find(letter) + 13

        if code > 26:
            #print(code)
            code -= 26
        else:
            pass    

    print(new_letters)
    print(code)
    #print(new_letters)
'''
        for nums in code:
            transform = code.find(nums) + 13

        
        get index value
        add 13 to index value
        if index exceeds 26, subtract 26 from new index value
        get new letter
        '''

lions = True
while lions == True:
    print("Hello! We're on a secret mission!\n")
    message = input("What's the message I need to encrypt? Or press enter to quit.")

    if message == '':
        print("Sayonara!")
        quit()
    else:
        message.lower()
        doom()