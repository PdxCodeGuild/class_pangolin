#Bieschke Lab 20: Credit Card Validation 
'''
Lab 20: Credit Card Validation
Write a function which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:

Convert the input string into a list of ints
Slice off the last digit. That is the check digit.
Reverse the digits.
Double every other element in the reversed list.
Subtract nine from numbers over nine.
Sum all values.
Take the second digit of that sum.
If that matches the check digit, the whole card number is valid.
'''
lion = True
while lion == True:
    print("Hello! Are you worried about your credit card number? Worry no more!")
    numbah = input("Type your credit card number here, and I'll check it!")

    if numbah == '':
        print("Sayonara!")
        quit()

    elif len(numbah) != 16: 
        print("Credit cards have 16 digits") 
        continue

    liszt = list(numbah)
    check_digit = liszt.pop()
    liszt.reverse()

#Converts the string in liszt into ints and saves it as a new list 
    liszt2 = [int(x) for x in liszt]

#checks index of lizst2 with a tuple
    liszt2 = [x*2 if i%2 == 0 else x for i, x in enumerate(liszt2)]

    liszt2 = [x - 9 if x > 9 else x for x in liszt2]

    tiger = sum(liszt2)
    tiger = str(tiger)
    tiger = list(tiger)

    validate = tiger[1]
    if validate == check_digit:
        print("Valid!")
    else:
        print("You were right to worry!") 
        print("The check digit does not match the validation digit!")