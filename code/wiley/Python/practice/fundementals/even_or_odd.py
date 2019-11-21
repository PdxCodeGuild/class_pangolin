#Write a function that tells whether a number is even or odd (hint, compare a/2 and a//2, or use a%2)

def even_or_odd():
    num = int(input("Give me a number.\n"))
    if num % 2 == 0:
        print("even")
    else:
        print("odd")
even_or_odd()