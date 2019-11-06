# Shawn Stolsig
# PDX Code Guild
# Assignment: Optional Lab - Arbitrary Precision Arithmetic
# Date: 11/6/2019

# addition

# get input
def get_input():
    while True: 
        # get num1 input, checking to make sure it's an int
        try:
            num1 = int(input("What is the first number? "))
            break
        except ValueError: 
            print("You did not input a whole number, please try again.")

    while True:
        # get num2 input, checking to make sure it's an int
        try:
            num2 = int(input("What is the second number? "))
            break
        except ValueError: 
            print("You did not input a whole number, please try again.")

    return num1,num2

# do elementary addition
def do_addition(num1, num2):

    # create reverse lists of ints of each number
    num1_list = list(str(num1))
    num1_list = [int(n) for n in num1_list]
    num1_list.reverse()
    num2_list = list(str(num2))
    num2_list = [int(n) for n in num2_list]
    num2_list.reverse()

    # declare an empty list for holding sum
    sum_list = []

    # if num1 is a longer number 
    if len(num1_list) > len(num2_list):
        # declare an int for carrying over tens place
        carry = 0
        # iterate through shorter num2
        for i in range(len(num2_list)):

            # create this sum by adding digits from both list plus the carry
            this_sum = num1_list[i] + num2_list[i] + carry
            # append a digit to sum_list representing the ones place
            sum_list.insert(i,this_sum%10)
            # set carry equal to the number of 10s
            carry = this_sum // 10

        # iterate through remaining numbers in num1
        for j in range(i+1,len(num1_list)):
            # create this sum by adding digit from longer list plus the carry
            this_sum = num1_list[j] + carry             # should only have carry on first character
            # append a digit to sum_list representing the ones place
            sum_list.insert(j,this_sum%10)
            # set carry equal to the number of 10s
            carry = this_sum // 10

        # if num1 is a longer number 
    
    if len(num2_list) >= len(num1_list):
        # declare an int for carrying over tens place
        carry = 0
        # iterate through shorter num2
        for i in range(len(num1_list)):

            # create this sum by adding digits from both list plus the carry
            this_sum = num2_list[i] + num1_list[i] + carry
            # append a digit to sum_list representing the ones place
            sum_list.insert(i,this_sum%10)
            # set carry equal to the number of 10s
            carry = this_sum // 10

        # iterate through remaining numbers in num1
        for j in range(i+1,len(num2_list)):
            # create this sum by adding digit from longer list plus the carry
            this_sum = num2_list[j] + carry             # should only have carry on first character
            # append a digit to sum_list representing the ones place
            sum_list.insert(j,this_sum%10)
            # set carry equal to the number of 10s
            carry = this_sum // 10
    
    # if there is any remaining carry, append it to sum list.  
    # this only happens when you add two single digits and they sum greater than 10
    if carry == 1:
        sum_list.append(1)

    # reverse list back to normal order and join together
    sum_list.reverse()
    
    sum_list = [str(num) for num in sum_list]
    return_sum = ''.join(sum_list)

    # return 
    return int(return_sum)



    # return result

# main
num1, num2 = get_input()

print(f"{num1} + {num2} = {do_addition(num1,num2)}")