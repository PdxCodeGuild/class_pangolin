# Shawn Stolsig
# PDX Code Guild 
# Assignment: Intro Class Lab 4 - Grading
# Date: 10/23/2019

import random

# get input number grade

numGrade = int(input("please input number grade: "))
rivalGrade = random.randint(0,100)

# init letter grade to x 
letterGrade = 'x'

# exit if not a valid grade
if not numGrade in range(0,101):
    print("invalid grade, quitting")
    exit()

# determine letter grade with if statements
if numGrade <=100 and numGrade >= 90:
    letterGrade = 'A'
elif numGrade <= 89 and numGrade >= 80:
    letterGrade = 'B'
elif numGrade <= 79 and numGrade >= 70:
    letterGrade = 'C'
elif numGrade <= 69 and numGrade >= 60:
    letterGrade = 'D'
elif numGrade < 60 and numGrade >= 0:
    letterGrade = 'F'

# determine wither you got a plus or minus
onesDigit = numGrade % 10

if letterGrade == 'F':
    pass  # do nothing, we don't want to add a plus or minus 
elif numGrade == 100:
    letterGrade += '+'   # scoring a 100 is an A+, not an A-
elif onesDigit == 9 or onesDigit == 8 or onesDigit == 7:
    letterGrade += '+'
elif onesDigit == 2 or onesDigit == 1 or onesDigit == 0:
    letterGrade += '-'
    
# print your letter grade
print(f"your grade is {letterGrade}")

# conditional expression to handle program output....different message depending if you win or lose
print(f"you scored better!  you got a {numGrade} while your rival got a {rivalGrade}") if numGrade > rivalGrade else print(f"your rival beat you with a {rivalGrade}")

