# Taylor Rebbe
# PDX Coed Guild
# Lab_10v2
# 10/25/2019

# Variables
message1 = "\nEnter a number (0 - 999): > "

# User input
usr_inp1 = input(message1)

num = usr_inp1

# Number to English dictionaries
num_sgl = {
     "0": "Zero",
     "1": "One",
     "2": "Two",
     "3": "Three",
     "4": "Four",
     "5": "Five",
     "6": "Six",
     "7": "Seven",
     "8": "Eight",
     "9": "Nine"
}
num_dbl = {
     "0": "Ten",
     "1": "Eleven",
     "2": "Twelve",
     "3": "Thirteen",
     "4": "Fourteen",
     "5": "Fifteen",
     "6": "Sixteen",
     "7": "Seventeen",
     "8": "Eighteen",
     "9": "Nineteen"
}
num_tns = {
     "2": "Twenty",
     "3": "Thirty",
     "4": "Fourty",
     "5": "Fifty",
     "6": "Sixty",
     "7": "Seventy",
     "8": "Eighty",
     "9": "Ninety",
}

# Get lenghth of the input string
def getInpLen(num_str):
    return len(str(num_str))

# Converts the inputs into a list
def numToList(usr_inp1):
    return list(usr_inp1)

# Compares the dictionary and list for Key matches
def getNumDict(num_dict, num):
    for key, value in num_dict.items():
     if key == num:
         return value

# Gents the value for double digits
def getTensValue(usr_inp1):
    if numToList(usr_inp1)[0] == "1":
        pos1 = getNumDict(num_dbl, numToList(usr_inp1)[1])
        print(pos1)
    elif numToList(usr_inp1)[1] != "0":
        pos1 = getNumDict(num_tns, numToList(usr_inp1)[0])
        pos2 = getNumDict(num_sgl, numToList(usr_inp1)[1])
        print(f"{pos1}-{pos2}")
    else:
        pos1 = getNumDict(num_tns, numToList(usr_inp1)[0])
        print(pos1)

# Gets the value for 3 digits
def getHunValue(usr_inp1):
    if numToList(usr_inp1)[1] == "0":
        if numToList(usr_inp1)[2] == "0":
            pos1 = getNumDict(num_sgl, numToList(usr_inp1)[0])
            print(f"{pos1}-Hundred")
        else:
            pos1 = getNumDict(num_sgl, numToList(usr_inp1)[0])
            pos3 = getNumDict(num_sgl, numToList(usr_inp1)[2])
            print(f"{pos1}-Hundred-{pos3}")
    elif numToList(usr_inp1)[1] == "1":
        pos1 = getNumDict(num_sgl, numToList(usr_inp1)[0])
        pos2 = getNumDict(num_dbl, numToList(usr_inp1)[2])
        print(f"{pos1}-Hundred-{pos2}")
    elif numToList(usr_inp1)[1] != "1":
            if numToList(usr_inp1)[2] != "0":
                pos1 = getNumDict(num_sgl, numToList(usr_inp1)[0])
                pos2 = getNumDict(num_tns, numToList(usr_inp1)[1])
                pos3 = getNumDict(num_sgl, numToList(usr_inp1)[2])
                print(f"{pos1}-Hundred-{pos2}-{pos3}")
            else:
                pos1 = getNumDict(num_sgl, numToList(usr_inp1)[0])
                pos2 = getNumDict(num_tns, numToList(usr_inp1)[1])
                print(f"{pos1}-Hundred-{pos2}")

# Main program
if getInpLen(usr_inp1) == 1:
    print(getNumDict(num_sgl, usr_inp1))

if getInpLen(usr_inp1) == 2:
    getTensValue(usr_inp1)

if getInpLen(usr_inp1) == 3:
    getHunValue(usr_inp1)
   