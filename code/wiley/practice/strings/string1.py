#Get a string from the user, print out another string, doubling every letter.



def doubleletter(var1):
    
    y =[x*2 for x in var1]
    z = ''
    z = str(z).join(y)
    return z

var1 = input("What word would you like to manipulate?")
print(doubleletter(var1))