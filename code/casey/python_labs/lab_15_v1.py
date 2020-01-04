'''
Lab 15: Number to Phrase - Version 1

Purpose/goal: Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.

    - Use modulus to extract the ones and tens digit. - D

    - Use the digit as an index for a list of strings OR as a key for a dict of digit:phrase pairs. - D

'''

# user greeting
print("\nHello! This is a simple program that turns numbers into words!\n")

# define num_to_phrase function
def num_to_phrase():
    # create num_dict
    num_dict = {1:"One", 2:"Two", 3: "Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine", 10:"Ten",
    11:"Eleven", 12:"Twelve", 13:"Thirteen", 14:"Fourteen", 15:"Fifteen", 16:"Sixteen", 17:"Seventeen", 18:"Eighteen", 19:"Nineteen",
    20:"Twenty", 30:"Thirty", 40:"Fourty", 50:"Fifty", 60:"Sixty", 70:"Seventy", 80:"Eighty", 90:"Ninety"}

    # request int from user
    num = int(input("Please enter a number between 1 & 1000 you'd like to see in words: "))

    # prints numbers 1-19 in words
    if 1 <= num <19:
        print(f"\nYour number is: {num_dict[num]}\n")

    # handles numbers 20-99 using modulus & prints user number in words
    if 20 <= num < 100:
        x = num // 10
        y = num % 10
        if x == 1:
            print(f"\nYour number is: {num_dict[num]}\n")
        else:
            x *= int(10)
            print(f"\nYour number is: {num_dict[x]} {num_dict[y]}\n")

    # for x in num_dict:
    #     if x == num:
    #         print(f"\nYour number is: {num_dict[num]}\n")
    
    # else: 
    #     quit()

# calls num_to_phrase funtion to kick off program
num_to_phrase()