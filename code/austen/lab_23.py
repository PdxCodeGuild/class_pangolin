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

    # name.append(find_it)
    # return name
    # if find_it in things:
    #     print dict(find_it)

#print (find_stuff())
# things.append(input_stuff())
# print (things)

what_to_do = (input('What would you like to do? (create,find,update,delete)'))

if what_to_do == 'create':
    input_stuff()
elif what_to_do == 'find':
    find()
  




'''    
#  Create a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.
    for
# Retrieve a record: ask the user for the contact's name, find the user with the given name, and display their information
    for
# Update a record: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.
    for
# Delete a record: ask the user for the contact's name, remove the contact with the given name from the contact list.
'''