import random
def random_name():
    name= ''
    phonetic = ['s','t','r','ch','g','qu','th','m','n','mn','b','sh','st','w','x','z','v','h','b','j','l']
    phonetic2 = ['e','a','y','o','oo','u','ou','i','ie','ae','ee','ey']
    for i in range(random.randint(1,4)):
        name += random.choice(phonetic)+random.choice(phonetic2)
    return name
print(random_name())
    
    