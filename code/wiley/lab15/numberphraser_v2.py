#Make a function to convert a given number into its english representation.
#For example: 67 becomes 'sixty-seven'. Handle numbers from 0-999.
#Hint: you can use modulus to extract the ones and tens digit.
#Hint 2: use the digit as an index for a list of strings OR as a key for a dict of digit:phrase pairs.
#Version 2: Handle numbers from 100-999.


ones_digit_dict = {0: "", 1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
teens_digit_dict = {10:"Ten", 11: "Eleven", 12:"Twelve",13:"Thirteen",14:"Fourteen",15:"Fifteen",16:"Sixteen",17:"Seventeen",18:"Eighteen",19:"Nineteen"}
tens_digit_dict = {0: "",2:"Twenty", 3:"Thirty",4:"Forty",5:"Fifty",6:"Sixty",7:"Seventy",8:"Eighty",9:"Ninety"}
#make dict for hundreds digits
hundreds_digit_dict = {1: "One Hundred", 2:"Two Hundred", 3:"Three Hundred", 4:"Four Hundred", 5: "Five Hundred",6:"Six Hundred", 7:"Seven Hundred",8:"Eight Hundred",9:"Nine Hundred"}
#make function to take in number inputs

def phraser ():
    a = int(input("What is the number? \n")) #ask for input number, convert to a int

    hundreds_digit = a//100 #floor division by 100 gets us the hundreds digit
    hunds_tens_digit = a%100 #modulo by 10 gets us the tens digit, IF its a hundreds number
    tens_digit = (a%100)//10 #a %100 gets us the tens digit, floor division by 10.  
    ones_digit = a%10 #modulo by 10 gets us the one digit
    teens_range = range(10,20)
    #print(hundreds_digit, hunds_tens_digit, tens_digit, ones_digit)
    #print(tens_digit)
    if a ==0: #0 = zero
        return print("zero")
        
    if hundreds_digit in hundreds_digit_dict.keys(): 
        hundreds = hundreds_digit_dict.get(hundreds_digit) #finds the hundreds digit in the dictionary
        #print(hundreds) #hundreds test print
        if hunds_tens_digit in teens_range: #check for teens
            if hunds_tens_digit in teens_digit_dict.keys():
                big_teens = teens_digit_dict.get(hunds_tens_digit)
                print(f"{hundreds} {big_teens}")
                return
        elif tens_digit in tens_digit_dict.keys():
            #print(tens_digit_dict.get(tens_digit))
            tens = tens_digit_dict.get(tens_digit)
            if ones_digit in ones_digit_dict.keys():
                #print(ones_digit_dict.get(ones_digit))
                ones = ones_digit_dict.get(ones_digit)
                print(f"{hundreds} {tens} {ones}")
                return

            
        tens_digit in tens_digit_dict.keys()
        tens = tens_digit_dict.get(tens_digit)
           
        ones_digit in ones_digit_dict.keys()
        ones = ones_digit_dict.get(ones_digit)

        print(f"{hundreds} {tens} {ones}")
        return

            
    
    if a in teens_digit_dict.keys():
        return print(teens_digit_dict.get(a))
    if tens_digit in tens_digit_dict.keys():
        #print(tens_digit_dict.get(tens_digit))
        tens = tens_digit_dict.get(tens_digit)
    if ones_digit in ones_digit_dict.keys():
        #print(ones_digit_dict.get(ones_digit))
        ones = ones_digit_dict.get(ones_digit)
    print(f"{tens} {ones}")
    
phraser()