'''
credit card validation 02
written by Rhornberger
last updated oct 25 2019
'''
#turning my string of numbers into a list of intergers
num = input('Please enter a credit card number: ')
cc_num = [int(num) for num in num]
#print(cc_num)

#slicing the last number off of my list
cc_num1 = cc_num[slice(15)]
# allowing myself to recall the final number later
cc_num2 = cc_num[-1]
#checking my print outs to see what I have.
#print(cc_num)
#print(cc_num1)
#print(cc_num2)
#reversing the list
cc_num3 = []
for i in reversed(cc_num1):
    cc_num3.append(i)
#print(cc_num3)
#doubling every other element in the list
def multi(cc_num3):
    res = list(cc_num3)
    for i in range(len(res)):
        if i % 2 == 0:
            res[i] = res[i] * 2
    return res
cc_num4 = multi(cc_num3)
#print(cc_num4) 
#subtract 9 from all numbers over 9
def sub(cc_num4):
    res = list(cc_num4)
    for i in range(len(res)):
        if i <= 15 :
            res[i] = res[i] - 9 if res[i] > 9 else res[i]
    return res
cc_num5 = sub(cc_num4)
#print(cc_num5)
#sum all values
cc_num6 = sum(cc_num5)
#print(cc_num6)
#take the second digit of that sum
cc_num7 = str(cc_num6)
#print(cc_num7)
cc_num8 = cc_num7[-1]
#print(cc_num8)
cc_num8 = int(cc_num8)
#check digits
if cc_num8 / cc_num2 == 1:
    print('Congratulations! This is a valid credit card')
else:
    print(f'I am sorry {num} is not a valid credit card number. ')