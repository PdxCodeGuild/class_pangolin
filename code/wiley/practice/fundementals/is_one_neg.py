#Write a function that takes two ints, a and b, and returns True if one is positive and the other is negative.

def is_one_neg(a,b):
    
    if first > 0:
        if second <= 0:
            print("True!")
        if second >0:
            print("False!")
    else:
        if second > 0:
            print("True!")
        else:
            print("False!")
first = int(input("What is your first number>\n"))
second = int(input("What is your second number\n"))
is_one_neg(first, second)