#Convert the input string into a list of ints
#Slice off the last digit. That is the check digit.
#Reverse the digits.
#Double every other element in the reversed list.
#Subtract nine from numbers over nine.
#Sum all values.
#Take the second digit of that sum.
#If that matches the check digit, the whole card number is valid.

#example card number: 4556737586899855
#user card input
cardnums = input("What is your credit card number?")

#convert user card string into a list, print to check
cardnums_list = [int(cardnum) for cardnum in str(cardnums)]
#print(cardnums_list)

#slice the last digit, save to check for later
check_digit = cardnums_list.pop()


#reverse the digits
cardnums_list.reverse()

#double every OTHER element in the list
cardnums_list = [num*2 if spot%2 == 0 else num for spot, num in enumerate(cardnums_list)]

#subtract nine from the numbers over nine
cardnums_list = [num-9 if num>9 else num for num in cardnums_list]

#sum all the values
cardnums_list_sum = sum(cardnums_list)

#take the second digit of that sum
#turning the list into a string, and then back into a list, thus making the digits split up
cardnums_string = str(cardnums_list_sum) 
cardnums_string = [nums for nums in cardnums_string] 

#check if second digit is same as the check digit
final_check = int(cardnums_string[1])
if final_check == check_digit:
    print("Valid Card Number.")
else:
    print("Invalid Number.")
    