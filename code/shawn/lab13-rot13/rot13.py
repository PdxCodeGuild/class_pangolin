# Shawn Stolsig
# PDX Code Guild 
# Assignment: Lab 19 - Rotation Cypher
# Date: 10/28/2019

# def function for encoding in ROT13
def encode(user_input, passed_cipher):
    ''' this function receives an input string and converts it to ROT13, returning the converted string '''

    # declare return string
    return_str = ''

    # iterate through each char in input string
    for char in user_input:
        # if an empty space, add empty space to new string
        if char == ' ':
            return_str += " "
        # if not a space, concatenate the encoded character
        else:
            return_str += passed_cipher[ord(char)-97][1]

    # return encoded string
    return return_str

# function to build the cipher based on how user wants to rotate characters
def build_cipher(rot):

    # declare cipher, which will be a list of tuples
    my_cipher = []

    # iterate through alphabet, index 0 to 25
    for i in range(0,25):
        # create two variables that will become a tuple
        char_1 = i + 97                 # 97 is 'a' in ASCII
        char_2 = i + 97 + rot           # add the rotation value to the ASCII value of character

        # wrap chars around if they go above 'z'
        if char_1 > 122:
            char_1 -= 26
        if char_2 > 122: 
            char_2 -= 26

        # append tuple to cipher
        my_cipher.append(   (chr(char_1), chr(char_2))  )

    # return cipher
    return my_cipher


# main
while True:
    # get desired rotation input and build cipher
    input_rot = int(input("What rotation value?: "))
    cipher = build_cipher(input_rot)

    # get input string and print encoded version
    input_string = input("What string would you like to encode? ")
    print(encode(input_string, cipher))

    # decide if program keeps running or not
    keep_running = input("Enter to quit or input anything to continue")
    if not keep_running:
        break
print("quitting")

