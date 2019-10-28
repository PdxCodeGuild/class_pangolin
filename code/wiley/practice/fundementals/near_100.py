#Write a function that returns True if a number within 10 of 100.

def near_100():
    num = int(input("What is your number?\n"))
    near_range = range(90,111)
    if num  in near_range:
        print("True")

    else:
        print("False")
near_100()