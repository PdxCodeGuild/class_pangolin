with open('test_contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    lines = [item.lower() for item in lines]
    #print(lines)

things = [] 

for i in range(1,3):
    key_things = lines[0]
    key_things = key_things.split(',')
    #print(key_things)
    row = lines[i]
    row = row.split(',')
    row = dict(zip(key_things,row))
    things.append(row)
#print(things)

#print (things) # rememeber to put the print statement outside the for loop or you will end up printing every time the loop itterates 
def input_stuff():
    user = []
    user_input = input('what is your name? '), input('what is your favorite fruit? '), input('what is your favorite color?')
    new_row = ''.join(user_input).split(',')
    user.append(user_input)
    user = [list(x) for x in user]
    user = [value for sec_list in user for value in sec_list]
   # print(user)
    new_row = dict(zip(key_things, user))
    things.append(new_row)
    print(things)
    return new_row

def find():
    find_it = input('What is the name of the person you would like to find? ')
    for n in things:
        if n['name'] == find_it:
            print (n)
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
            # return n  
            
def delete():
    delete = input('What contatct name do you want to delete? ')
    for i in range(len(things)):
        if things[i]['name'] == delete:
            del things[i]
            print(things)
            return things


while True:
    what_to_do = (input('\nWhat would you like to do? (create,find,update,delete)\nenter [c, f, u, d] or done: '))

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

