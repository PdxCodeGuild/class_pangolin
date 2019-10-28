#Bieschke Lab 15: Number to Phrase v2 
#Bieschke Lab 15: Number to Phrase 
'''
Convert a given number into its english representation. 
For example: 67 becomes 'sixty-seven'. Handle numbers from 0-999.
'''

nums_exceptions = {0: "zero",
10: "ten",
11: "eleven",
12: "twelve",
13: "thirteen",
14: "fourteen",
15: "fifteen",
16: "sixteen",
17: "seventeen",
18: "eighteen",
19: "nineteen"
}

nums_singles = {1: "one",
2: "two",
3: "three",
4: "four",
5: "five",
6: "six",
7: "seven",
8: "eight",
9: "nine"
}

nums_tens = {2: "twenty",
3: "thirty",
4: "forty",
5: "fifty",
6: "sixty",
7: "seventy",
8: "eighty",
9: "ninety"
}
'''
can you do this with nums_singles plus the word hundred? I think I might
nums_hundreds = {1: 
2: 
3: 
4: 
5: 
6: 
7: 
8:
9:
}
'''
def cheq():
    if x == '':
        print("Sayonara!")
        quit()

    elif int(x) not in range(0, 1000): 
        print("Sorry, I need a number from 0 to 999") 
        quit()

lion = True
while lion == True:
    x = input("Hello! Enter any integer from 0-999. You can also press enter to quit.")
    cheq()
    x = int(x)

    if x in nums_exceptions:
        print(f"Your number is {nums_exceptions[x]}")
        print("*"*100)
        continue

    elif x in nums_singles:
        print(f"Your number is {nums_singles[x]}")
        print("*"*100)
        continue  
    
    elif x in range(20, 100):
        x = str(x)
        x = list(x)
        tens = x[0]
        tens = int(tens)
        singles = x[1]
        singles = int(singles)
        print(f"{tens}{singles}")

        print(f"Your number is {nums_tens[tens]}", end='-')

        print(f"{nums_singles[singles]}")
        continue

    else:
        x = str(x)
        x = list(x)
    
        hundreds = x.pop(0)
        hundreds = int(hundreds)


        x = [str(x) for x in x]
        print(x)
        x = int(''.join(x))
        print(x)
        if x in nums_exceptions:        
            print(f"Your number is {nums_singles[hundreds]} hundred {nums_exceptions[x]}")
            continue
        elif x in nums_singles:
            print(f"Your number is {nums_singles[hundreds]} hundred {nums_singles[x]}")
            continue

        x = str(x)
        x = list(x)

        tens = x[0]
        tens = int(tens)
        singles = x[1]
        singles = int(singles)
        print(f"{hundreds}{tens}{singles}")
        print(f"Your number is {nums_singles[hundreds]} hundred", end=' ')
        print(f"{nums_tens[tens]}", end=' ')
        print(f"{nums_singles[singles]}")
        continue
