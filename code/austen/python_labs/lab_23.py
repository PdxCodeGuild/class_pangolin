with open('test_contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    print (lines)
    lines = [item.lower() for item in lines]
    print(lines)
    #print(lines)

things = [] 

for i in range(len(lines)):
    key_things = lines[0]
    key_things = key_things.split(',')
    print(key_things)
    row = lines[i]
    row = row.split(',')
    row = dict(zip(key_things,row))
    things.append(row)
#print(things)
def export_list():
    global things
    mylist = []
    
    things[0].values()
    list(things[0].values())
    list(things[1].values())
    things[0].keys()
    ','.join(things[0].keys())
    ','.join(things[0].values())
    mylist.append(','.join(things[0].keys()))
    for i in range(len(things)):# this for loop makes it loop through everything and not just line one and two
        mylist.append(','.join(things[i].values()))
    '\n'.join(mylist)
    print(mylist)
    # print (mylist)
    with open('test_contacts_out.csv', 'w') as contact_list:
       contact_list.write('\n'.join(mylist))

#print (things) # rememeber to put the print statement outside the for loop or you will end up printing every time the loop itterates 
def input_stuff():
    #user = []
    user = input('what is your name? '), input('what is your favorite fruit? '), input('what is your favorite color?')
    # new_row = ''.join(user_input).split(',')
    # user.append(user_input)
    # user = [list(x) for x in user]
    # user = [value for sec_list in user for value in sec_list]
    print(user)
    new_row = dict(zip(key_things, user))
    things.append(new_row)
    print(things)
    export_list()
    #return new_row

def find():
    find_it = input('What is the name of the person you would like to find? ')
    for n in things:
        if n['name'] == find_it:
            print (n)
            #export_list()
            return n
        
def update():
    update = input('what contact do you want to update? ')
    atrabute = input('what option do you want to update? ')
    new_value = input('what would you like to replace it with? ')
    for n in things:
        if n['name'] == update:
            if atrabute in n:
                n[atrabute] = new_value
                print (n)
                export_list()
            # return n  
            
def delete():
    delete = input('What contatct name do you want to delete? ')
    for i in range(len(things)):
        if things[i]['name'] == delete:
            del things[i]
            print(things)
            export_list()
            return things


while True:
    what_to_do = input('\nWhat would you like to do? (create,find,update,delete)\nenter [c, f, u, d] or done: ')

    if what_to_do == 'c':
        input_stuff()
    elif what_to_do == 'f':
        find()
    elif what_to_do == 'u':
        update()
    elif what_to_do == 'd':
        delete()
    elif what_to_do == 'done':
        break
    else:
        print(f'please enter a valid responce.')
        
#with open('test_contacts.csv', 'a') as file:
   # file.write()