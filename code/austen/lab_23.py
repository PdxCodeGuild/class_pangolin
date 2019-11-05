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

    #name = []
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
        if n['name'] == find_it:
            print (n)
            return n
        for i in range(len(n)):
            if n[i]['name'] == atrabute:
                #update
            elif n[i]['favorite fruit'] == atrabute:
                #update
            elif n[i]['favorite color'] == atrabute:
                #update
            #work on this one tomorrow

            
def delete():
    delete = input('What contatct name do you want to delete? ')
    for i in range(len(things)):
        if things[i]['name'] == delete:
            del things[i]
            print(things)
            return things

#print (find_stuff())
# things.append(input_stuff())
# print (things)

what_to_do = (input('What would you like to do? (create,find,update,delete)'))

if what_to_do == 'create':
    input_stuff()
elif what_to_do == 'find':
    find()
elif what_to_do == 'update':
    update()
elif what_to_do == 'delete':
    delete()
else:
    print('please enter a valid responce. ')




'''    
#  Create a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.
    for
# Retrieve a record: ask the user for the contact's name, find the user with the given name, and display their information
    for
# Update a record: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.
    for
# Delete a record: ask the user for the contact's name, remove the contact with the given name from the contact list.
'''