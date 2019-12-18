#bieschke gonna work this time 
#currently writes line 34 to heroes_out.csv
'''
Version 3
When REPL loop finishes, write the updated contact info to the CSV file to be saved. 
'''
hero = []
with open('heroes.csv', 'r+') as file:
    lines = file.read().split('\n')
    keys = lines[0].split(',')      #pulls off the header row
    for i in range(1, len(lines)):
        values = lines[i].split(',')    #pulls off the data rows
        hero.append(values)

def hero_dict(keys, hero):
    heroes = []     #sets a list for dictionaries
    for i in range(0, len(hero)):
        for key in keys:
            names = dict(zip(keys, hero[i]))    #zips the lists of keys and values(hero) together by index
        heroes.append(names)
    return heroes

def search(hero, query):
    for arr in hero:
        if arr[0] == query:
            return arr
    else:
        print("Not found")

def save(*args):
    for i in range(len(hero)):
    #for hero in heroes:
        #hero_out.append(hero_out)
        hero_out = [",".join(keys)]
        hero_out.append(hero_out)
    #hero_out = ['k1,k2', 'v1, v2']  #think about how the data needs to be formatted to look like this
    file = open("heroes_out.csv", "w")
    hero_out = str(hero_out).strip("'[]'")
    file.write(hero_out)
    #file.write('\n'.join(hero_out))
    file.close()
    print("Your changes have been saved!")

# lions = True
# while lions:
while True:    
    print("Hello! Today we're working with a list of historical generals.")
    action = input("You can create, retrieve, update, or delete a record, or enter q or 1 to quit.\n>")
    
    if action in ('c', 'create'):
        name = input("Name: ")
        location = input("Location: ")
        era = input("Era: ")
        conquest = input("Conquest: ")
        action_list = [name, location, era, conquest]
        hero.append(action_list)
        print(f"The generals entered are:\n {hero}")
    
    elif action in ('r', 'retrieve'):
        info = input("Whose information would you like to see?")
        #info = 'Ghenghis Khan'
        print(search(hero, info))
    
    elif action in ('u', 'update'):
        info = input("Whose information would you like to see?")
        new_value = search(hero, info)
        field = input("Which field would you like to update?")
        lower_keys = [key.lower() for key in keys]
        if field in lower_keys:
            new_conquest = input("Enter your update: ")
            new_value[lower_keys.index(field)] = new_conquest
            print(new_value)
        else:
            print("Sorry, that field cannot be edited.")

    elif action in ('d', 'delete'):
        info = input("Whose information would you like to delete?")
        del_value = search(hero, info)
        confirm = input("Enter 'd' to delete this entry: ")
        if confirm == 'd':
            hero.remove(del_value)
        else: 
            continue

        print(hero)
        
    elif action in ('q', '1'):
        save(keys, hero)
        quit()

print(hero_dict(keys, hero))
save()

'''
maplist = [{0: 'a'}, {1: 'b'}]
maplist[0][0] = 'z'

dict(zip(keys, values))
'''

