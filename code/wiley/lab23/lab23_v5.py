import os
filename = "contacts.csv"
filename_out = "contacts2.csv"
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), filename), 'r+') as file:
    lines = file.read().split('\n')
    #print(lines)
#turn the csv into a list of dictionaries

contact_list = []
keys = lines[0].split(',')
values = [x.lower().split(',') for x in lines[1:]]

for value in values:
    contact_list.append(dict(zip(keys, value)))
def save_csv(x):
    '''This function takes in a string variable and writes to a txt file.'''
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), filename_out), 'w') as file:
        file.write(x)
#make functions for Create, Retrieve, Update, and Delete
def create():
    '''This function will create a new contact(dictionary) in contact_list '''
    user_name = input("What is the name of the Contact?\n")
    user_age = input("What is the age of the Contact?\n")
    user_list = [user_name,user_age]
    for value in values:
        user_dict = (dict(zip(keys, user_list)))
    contact_list.append(user_dict)
    return contact_list

def retrieve():
    '''This function will return the desired contact's dictionary. '''
    get_contact = input("Whose contact information do you want to see?\n").lower()
    for contact in contact_list:        
        if contact["name"] == get_contact:
            print(contact)
            return 
    if contact["name"] != get_contact:
            print("Contact not in the contacts list.")
            pass

def update():
    '''This function will update a contact's information in contact list'''
    get_contact = input("Whose contact information do you want to see?\n").lower()
    not_found = True
    while not_found:
        for i in range(len(contact_list)):        
            if contact_list[i]['name'] == get_contact:
                
                user_update = input(f"Would you like to update {contact_list[i]['name']}'s name or {contact_list[i]['name']}'s age\n").lower()
                if user_update == 'age':
                    new_age = input("What is the new age?\n")
                    contact_list[i]['age'] = new_age
                    print(contact_list[i])
                    not_found = False
                    break
                if user_update == 'name':
                    new_name = input("What is the new name?\n")
                    contact_list[i]['name'] = new_name
                    not_found = False
                    break
                
                
                break
                
        if contact_list[i]["name"] != get_contact:
            print(f"{get_contact} not in the contacts list.")
            break
        
    return contact_list

def delete():
    '''This function will delete a contact's information in contact list.'''
    delete_contact = input('Whose information do you want to delete from the contacts list?\n').lower()        
    for i in contact_list:
        if i['name'] == delete_contact:
            contact_list.remove(i)
    print(contact_list)
            
    return contact_list

#Make a format function to bring the dictionary back into CSV form
def format_csv(x):
    '''This function will take in a list of dictionaries as an argument 
    and return them into a csv format'''
    
    global csv
    csv = ''
    my_keys = []
    my_values = []    
    for i in range(len(x)):
        my_values.append(list(x[i].values()))
    my_keys.append(list(x[0].keys()))
    my_keys_str = ''.join(','.join(elem) for elem in my_keys) + '\n'
    my_values_str = '\n'.join(','.join(elem) for elem in my_values)
    
    csv += (my_keys_str)
    csv += (my_values_str)
    return csv

#implement CRUD functions into a REPL loop
def crud():
    '''Uses the above functions with a whlie loop to allow users to choose which mode
    and edit the contact list. '''
    while True:
        user_select = input('''        Welcome to the contact list menu. 
        Type 'C' to create a new contact.
        Type 'R' to retrieve a contact's information.
        Type 'U' to update a contact's information.
        Type 'D' to delete a contact.
        Type 'E' to exit the program. ''').lower()
        if user_select == 'c':
            create()
            format_csv(contact_list)
            #save_csv(csv)            
        elif user_select == 'r':
            retrieve()
        elif user_select == 'u':
            update()            
            format_csv(contact_list)
            #save_csv(csv)
        elif user_select == 'd':
            delete()
            print(contact_list)
            format_csv(contact_list)
            print(csv)
            #save_csv(csv)
        elif user_select == 'e':
            print("Exiting program.  Goodbye.")
            save_csv(csv)

            break
        else:
            print("Not a valid selection")
            continue

crud()

