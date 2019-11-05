#BieschkeLab23 contact dictionary 

def hero_dict(keys, hero):
    heroes = []     #sets a list for dictionaries
    for i in range(0, len(hero)):
        for key in keys:
            names = dict(zip(keys, hero[i]))    #zips the lists of keys and values(hero) together by index
        heroes.append(names)
    return heroes
    #print(names)

def search(hero, query):
    #print(query)
    
    print('hero:',hero)
    for arr in hero:
        print('arr',arr)
        if arr[0] == query:
        #if hero.index(arr) == info:
            return arr
    else:
        print("Not found")

lions = True
while lions == True:
    hero = []
    print("Hello! Today we're working with a list of historical generals.")
    action = input("You can create, retrieve, update, or delete a record, or enter q or 1 to quit.\n>")
    
    with open('heroes.csv', 'r') as file:
        lines = file.read().split('\n')
        #print(lines)

        keys = lines[0].split(',')      #pulls off the header row
        #print(lines)
        #print(keys)
        for i in range(1, len(lines)):
            values = lines[i].split(',')    #pulls off the data rows
            #print(values)
            hero.append(values)
        #print(keys, hero)
        #print(hero)
        
    
    if action == 'c': #or 'create'
        name = input("Name: ")
        location = input("Location: ")
        era = input("Era: ")
        conquest = input("Conquest: ")
        action_list = [name, location, era, conquest]
        hero.append(action_list)
        print(f"The generals entered are:\n {hero}")
    
    elif action == 'r': #or 'retrieve'
        # info = input("Whose information would you like to see?")
        info = 'Ghenghis Khan'
        print(hero)
        print(search(hero, info))
        # if info in hero:
        #     print(hero)
        #else:
         #   print("That general has not been entered yet.")
    
    elif action == 'u': #or 'update'
        info = input("Whose information would you like to see?")
        print(search(hero, info))
        field = input("Which field would you like to update?")
        if field == 'conquest':
            new_conquest = input("Enter your update: ")
            hero[3] = new_conquest
            print(hero)
        else:
            print("Sorry, that field cannot be edited.")
        #crosscheck the input to the index of the desired field
            #recompile the list of the general's attributes
            #overwrite the previous entry
            #print the updated entry
        # else:
        #     print("That general has not been entered yet.")
        #     pass

    elif action == 'd': #or delete
        info = input("Whose information would you like to delete?")
        print(search(hero, info))
        #if info in hero:
        #    print(hero)
        confirm = input("Enter 'd' to delete this entry: ")
        if confirm == 'd':
            hero.remove(info)
        else: 
            continue
        # else:
        #     print("That general has not been entered yet.")
        #     pass
        
    elif action == 'q' or 1:
        quit()


print(hero_dict(keys, hero))
'''
maplist = [{0: 'a'}, {1: 'b'}]
maplist[0][0] = 'z'

dict(zip(keys, values))
'''