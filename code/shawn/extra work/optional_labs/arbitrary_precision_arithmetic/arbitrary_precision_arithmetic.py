# Shawn Stolsig
# PDX Code Guild
# Assignment: Optional Lab - Arbitrary Precision Arithmetic
# Date: 11/6/2019

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

# do long multiplication
def do_long_multiplication(num1, num2):

    # get reversed int lists for each num
    num1_list = list(str(num1))
    num1_list = [int(n) for n in num1_list]
    num1_list.reverse()
    num2_list = list(str(num2))
    num2_list = [int(n) for n in num2_list]
    num2_list.reverse()

    # figure out which list is shorter, and make that num1
    if len(num1_list) > len(num2_list):
        num3_list = num1_list.copy()
        num1_list = num2_list.copy()
        num2_list = num3_list.copy()

    # set up final product list
    product_list = []

    # we'll iterate through each number in shorter num list
    for i in range(len(num1_list)):
        # declare/reset carry
        carry = 0
        # set up this product list, which will be appended to main product list later
        this_product_list = []
        # iterate through each number of larger int
        for j in range(len(num2_list)):

            # get the product of the two
            this_product = num1_list[i] * num2_list[j]
            # add carry to the product
            this_sum = this_product + carry
            # get how many times 10 divides into the product
            carry = this_sum // 10
            # append string list with this_sum modulus 10
            # print(f"n1: {num1_list[i]} n2: {num2_list[j]} this_product: {this_product} this_sum {this_sum} carry: {carry}")
            this_product_list.append(this_sum%10)

    
        # append any leftover carry value to product
        if carry != 0:
            this_product_list.append(carry)
        
        # translate this_product_list into a joined, correctly-ordered int
        this_product_list.reverse()

        # add 0s to the end of the product for the number of i 
        for k in range (0,i):  
            this_product_list.append(0)
        this_product_list = [str(num) for num in this_product_list]

        # translate this product to the product list
        product_list.append(int(''.join(this_product_list)))

    # go through and add product lists together
    running_sum = product_list[0]
    for x in range(1,len(product_list)):
        # use elementary addition function
        running_sum = do_addition(running_sum, product_list[x])

    # return the sum of each individual product
    return running_sum

# main loop

while True:
    # get input
    num1, num2 = get_input()

    print(f"{num1} + {num2} = {do_addition(num1,num2)}")
    print(f"{num1} * {num2} = {do_long_multiplication(num1,num2)}")

    if not input("Press enter to quit or input anything to continue...."):
        break

print("Program ending.")