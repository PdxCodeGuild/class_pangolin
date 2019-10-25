
#this is the welcome statement to introduce your user to the program
print('*Welcome to the number to number name converter 1000*')
#define the what you want to call your game or program
def number_name():
    # dictionary, write nums to represent each side (int: str) in this case it is the number and then its spelling *notice 20-90 are only written in tens that is becasue below it is converted into full numbers : these are variables
    nums = {1:"One", 2:"Two", 3:"Three" ,4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight",      9:"Nine", 0:"Zero", 10:"Ten", 11:"Eleven", 12:"Tweleve" , 13:"Thirteen",                    14:"Fourteen", 15: "Fifteen", 16:"Sixteen", 17:"Seventeen", 18:"Eighteen",                  19:"Nineteen", 20:"Twenty", 30:"Thirty", 40:"Forty", 50:"Fifty", 60:"Sixty",                70:"Seventy", 80:"Eighty", 90:"Ninety"}
# below your variables you need to ask the user what you want them to do in this case we want them to add a number 
    num = int(input("Enter a number from 1-1000: "))
# To convert three digit number into words
    if 100 <= num < 1000:
        a = num // 100
        b = num % 100
        c = b // 10
        d = b % 10
        if c == 1 :
            print (nums[a] + " hundred" , nums[b])
        elif c == 0:
            print (nums[a] + " hundred" ,)
        else:
            c *= 10
            if d == 0:
                print (nums[a] + " hundred", nums[c])
            else:
                print (nums[a] + " hundred" , nums[c], nums[d])

# to convert two digit number into words 
    if 1 <= num <19:
        print (nums[num])

    if 20 <= num < 99:
        a = num // 10
        b = num % 10
        if a == 1:
            print (nums[num])
        else:
            a *= int(10)
            print (nums[a], nums[b])
# use the below statement to call the function
number_name()