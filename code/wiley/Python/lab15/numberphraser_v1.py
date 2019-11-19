#Make a function to convert a given number into its english representation.
#For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.
#Hint: you can use modulus to extract the ones and tens digit.
#Hint 2: use the digit as an index for a list of strings OR as a key for a dict of digit:phrase pairs.


#make dictionary for ten digits
#Still need to figure out how to deal with teens.  Hard code if begins with 1_?
tens_digit_dict = {0: "",2:"Twenty", 3:"Thirty",4:"Forty",5:"Fifty",6:"Sixty",7:"Seventy",8:"Eighty",9:"Ninety"}
teens_digit_dict = {10:"Ten", 11: "Eleven", 12:"Twelve",13:"Thirteen",14:"Fourteen",15:"Fifteen",16:"Sixteen",17:"Seventeen",18:"Eighteen",19:"Nineteen"}
#make dictionary for ones digits
ones_digit_dict = {0: "", 1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}

#make function to take in number inputs

def phraser ():
    a = int(input("What is the number? \n"))
    tens_digit = a//10
    ones_digit = a%10
    if a ==0:
        return print("zero")
    if a in teens_digit_dict.keys():
        return print(teens_digit_dict.get(a))
    if tens_digit in tens_digit_dict.keys():
        #print(tens_digit_dict.get(tens_digit))
        first = tens_digit_dict.get(tens_digit)
    if ones_digit in ones_digit_dict.keys():
        #print(ones_digit_dict.get(ones_digit))
        second = ones_digit_dict.get(ones_digit)
    return print(f"{first} {second}")
    
phraser()
