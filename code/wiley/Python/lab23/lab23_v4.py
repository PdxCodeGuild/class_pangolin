#Contact List lab23 version 2
#11/4/19
#Open the CSV, convert the lines of text into a list of dictionaries, on dictionary for each user.
#The text in the header represents the keys, the text in the other lines represents the values.
import os
filename = "contacts.csv"
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), filename), 'r+') as file:
    lines = file.read().split('\n')
    #print(lines)

#Make a list of keys from the first list in lines(the header)
contact_list = []
keys = lines[0].split(',')
#make a list of values
values = [x.lower().split(',') for x in lines[1:]]

#zip the lists together to create a dictionary for each contact
for value in values:
    #print(value)
    contact_list.append(dict(zip(keys, value)))

def format_to_csv(dictionary, keys):
    '''Takes 2 arguments and converts them into a csv formatted string. '''
    csv = ''
    
    csv += ','.join(keys)
    for row in dictionary:
        csv += ','.join(row) +'\n'
    
   
    
    return csv

def create():
    user_list = []
    print("You have selected create new record.\n")
    user_name = input("What is the name?\n")
    #user_address = input("What is the address?\n")
    #user_phone = input("What is the phone number?\n")
    #user_email = input("What is the email?\n")
    user_age = input("What is the age?\n")
    
    
    user_list = [user_name, user_age]
    temp_dict = dict(zip(keys, user_list))
    contact_list.append(temp_dict)
    #for value in user_list:    
    #    user_dict = (dict(zip(keys,value)))
    #contact_list.append(user_dict)
    #for element in contact_list:
    formatted_list = format_to_csv(element.values(), element.keys())
    #print(formatted_list)
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), filename), 'r+') as file:
        file.write(formatted_list)

def retrieve():
    print("You selected: Retrieve a record.\n")
    user_name = input("Whose contact information do you want to see?").lower()
    not_found = True
    #formatted_list = ''
    for element in contact_list:
        if element["name"]== user_name:
            print(element)
            not_found = False
            formatted_list = format_to_csv(element.values(), element.keys())
            #with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), filename), 'r+') as file:
            #    file.write(formatted_list)
    if not_found:
        print("Contact not found in contacts list.")

def update(): #maybe implement not_found flag
    print("You selected: Update a record. \n")
    user_name = input("Whose information would you like to update?\n").lower()
    not_found = True
    formatted_list = ''
    for i in range(len(contact_list)):
        if contact_list[i] == user_name:
            print(contact_list[i])
            update_element = input("User found! What part of their information would you like to update?\n").lower()
            if update_element in contact_list[i].keys():
                user_update = input(f"You want to update {element['name']}'s {update_element}? What is the update?\n")
                contact_list[i][update_element] = user_update
                not_found = False
                formatted_list = format_to_csv(contact_list[i].values(), contact_list[i].keys())
                with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), filename), 'r+') as file:
                    file.write(formatted_list)
            #if not_found:
             #   print('Option not found. ')
              #  pass
        #if not_found:
           # print("User not found.")
           # pass

def delete():
    print("You selected delete.\n")
    user_name = input("Whose information would you like to delete?\n").lower()
    not_found = True
    for element in contact_list:    
        if element["name"] == user_name:
            print(f"Deleting {user_name} from your contacts list.\n")
            contact_list.remove(element)
            not_found = False
            print(contact_list)
            break
    formatted_list = ''
    for element in contact_list:
        formatted_list += format_to_csv(list(element.values()), list(element.keys()))
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), filename), 'r+') as file:
        file.write(formatted_list)
    if not_found:
            print("Contact not found.")

def crud():
    while True:
        user_input = input("""What action would you like to complete?
    'C' for create new record.
    'R' for retrieve a record.
    'U' for update a record.
    'D' for delete a record.
    or 'EXIT' to close the program.""").lower()
        if user_input == 'c':
            create()
        elif user_input == 'r':
            retrieve()
        elif user_input == 'u':
            update()
        elif user_input == 'd':
            delete()
        elif user_input == 'exit':
            break
crud()