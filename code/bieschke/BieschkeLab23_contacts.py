#Bieschke Lab 23: contact dictionary 

def hero_dict(keys, hero):
    heroes = []     #sets a list for dictionaries
    for i in range(0, len(hero)):
        # for key in keys:
        names = dict(zip(keys, hero[i]))    #zips the lists of keys and values(hero) together by index
        heroes.append(names)
    return heroes
    #print(names)

with open('heroes.csv', 'r') as file:
    lines = file.read().split('\n')
    #print(lines)
    hero = []
    keys = lines[0].split(',')      #pulls off the header row
    #print(lines)
    #print(keys)
    for i in range(1, len(lines)):
        values = lines[i].split(',')    #pulls off the data rows
        #print(values)
        hero.append(values)
    #print(keys, hero)
    #print(hero)



print(hero_dict(keys, hero))

'''
heroes = []
with open("heroes.csv", 'r') as file:
    firstline = True    #deals with the keys first
    for line in file:
        if firstline == True:
            keys = "".join(line.split()).split(',')
            firstline = False
        else:
            values = "".join(line.split()).split(',')
            hero = {}
            for key in keys:
                print(key)
                hero[key] = hero[values]
            heroes.append(hero)
    print(heroes)
'''