# Taylor Rebbe
# PDX Code Guild
# Lab_10v2
# 10/25/2019
# Wanted to try it without the % and //... Things got out of hand O_o

# Variables
msg1 = "\nEnter a number (0 - 999): > "
msg2 = "Ctrl^C to exit\n"
msg3 = "I can't count that high :("
msg4 = "Error: Invalid number"
h = "-Hundred"

# Number to English dictionaries
sgl = {"0": "Zero","1": "One","2": "Two","3": "Three","4": "Four","5": "Five","6": "Six","7": "Seven","8": "Eight","9": "Nine"}
dbl = {"0": "Ten","1": "Eleven","2": "Twelve","3": "Thirteen","4": "Fourteen","5": "Fifteen","6": "Sixteen","7": "Seventeen","8": "Eighteen","9": "Nineteen"}
tns = {"2": "Twenty","3": "Thirty","4": "Forty","5": "Fifty","6": "Sixty","7": "Seventy","8":"Eighty","9": "Ninety",}

# Get lenghth of the input string
def inpLen(n_str):
    return len(str(n_str))

# Converts the inputs into a list
def numLst(inpS):
    return list(inpS)

# Compares the dictionary and list for Key matches
def getDct(dct, num):
    for x, y in dct.items():
     if x == num:
         return y

# Sources the dictionary given the position of the digit         
def pGet(dct, i):
    return getDct(dct, numLst(inpS)[i])

# Get the value for 2 digits
def twoDig(inpS):
    if numLst(inpS)[0] == "1":
        p1 = pGet(dbl, 1)
        print(p1)
    elif numLst(inpS)[1] != "0":
        p1 = pGet(tns, 0)
        p2 = pGet(sgl, 1)
        print(f"{p1}-{p2}")
    p1 = pGet(tns, 0)
    print(p1)

# Get the value for 3 digits
def thrDig(inpS):
    if numLst(inpS)[1] == "0":
        if numLst(inpS)[2] == "0":
            p1 = pGet(sgl, 0)
            print(f"{p1}{h}")
        p1 = pGet(sgl, 0)
        p3 = pGet(sgl, 2)
        print(f"{p1}{h}-{p3}")
    elif numLst(inpS)[1] == "1":
        p1 = pGet(sgl, 0)
        p2 = pGet(dbl, 2)
        print(f"{p1}{h}-{p2}")
    elif numLst(inpS)[1] != "1":
            if numLst(inpS)[2] != "0":
                p1 = pGet(sgl, 0)
                p2 = pGet(tns, 1)
                p3 = pGet(sgl, 2)
                print(f"{p1}{h}-{p2}-{p3}")
            p1 = pGet(sgl, 0)
            p2 = pGet(tns, 1)
            print(f"{p1}{h}-{p2}")

# Main loop
while True:
    try:
        inp = abs(int(input(msg1)))
        inpS = str(inp)
        print(msg2)
        if inp > 999:
            print(msg3)
        elif inpLen(inpS) == 1:
            print(getDct(sgl, inpS))
        elif inpLen(inpS) == 2:
            twoDig(inpS)
        elif inpLen(inpS) == 3:
            thrDig(inpS)
    except ValueError:
        print(msg4)
