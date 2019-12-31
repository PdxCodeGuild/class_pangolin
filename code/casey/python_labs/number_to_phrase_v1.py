'''
Lab 15: Number to Phrase - Version 1

Purpose/goal: Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.

    - Use modulus to extract the ones and tens digit.

x = 67
tens_digit = x//10
ones_digit = x%10

    - Use the digit as an index for a list of strings OR as a key for a dict of digit:phrase pairs.

'''

print("\nHello! This is a simple program that turns numbers into words!\n")

def num_to_phrase():
    num_dict = {1:"One", 2:"Two", 3: "Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine", 10:"Ten",
    11:"Eleven", 12:"Twelve", 13:"Thirteen", 14:"Fourteen", 15:"Fifteen", 16:"Sixteen", 17:"Seventeen", 18:"Eighteen", 19:"Nineteen",
    20:"Twenty", 30:"Thirty", 40:"Fourty", 50:"Fifty", 60:"Sixty", 70:"Seventy", 80:"Eighty", 90:"Ninety"}

    num = int(input("Please enter a number you'd like to see in words: "))

    for x in num_dict:
        if x == num:
            print(f"\nYour number is: {num_dict[num]}\n")
    
    else: 
        quit()

num_to_phrase()