#Write a function that returns the maximum of 3 parameters.

def max(a,b,c):
    num_list = []
    num_list.extend((a,b,c))
    num_list.sort()
    max_num = num_list[-1]
    print(str(max_num))
a= int(input("Give me a number\n"))
b= int(input("Give me a number\n"))
c= int(input("Give me a number\n"))
max(a,b,c)