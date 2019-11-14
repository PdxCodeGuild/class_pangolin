# Shawn Stolsig
# PDX Code Guild 
# Assignment: Practice 1 - Fundamentals
# Date: 10/25/2019

def is_even(a):
    print(a % 2 == 0)

# is_even(5)
# is_even(6)

def opposite(a,b):
    return (a < 0) or (b < 0)

# print(opposite(10, -1)) # True
# print(opposite(2, 3)) # False
# print(opposite(-1, -1)) #False

def near_100(num):
    return num >=90 and num <= 110

# print(near_100(50)) # False
# print(near_100(99)) # True
# print(near_100(105)) # True

def maximum_of_three(a, b, c):
    return max(a,b,c)

# print(maximum_of_three(5,6,2)) # 6
# print(maximum_of_three(-4,3,10)) # 10

def print_powers_2():
    for num in range(0,21):
        print(2**num, end = ", ") 

# print_powers_2()