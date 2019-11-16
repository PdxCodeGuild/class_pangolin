#Write a function that takes a string, and returns a list of strings, each missing a different character.

def remove_letter(a):
    b = [x for x in a]
    print(b)
    d = []
    for x in range(len(b)):
        #print(x)
        c = b.copy()
        c.pop(x)
        #print(c)
        (''.join(c))
        d.append(c)
    return d

        


var1 = input("GIMME A STRING, PUNK!\n")
print(remove_letter(var1))