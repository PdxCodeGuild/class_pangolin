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
    for key in keys:
        csv += key + ','
    csv = csv[:-1:1] + '\n'

    for row in dictionary:
        for column in row:
            csv += column + ','
        csv = csv[:-1] + '\n'
   
    
    return csv



def crud_loop():
    '''This function gives the user the option to Create Retrieve Update or Delete
     a record in the Contact List and returns the contact list in its new form. '''
   
    while True: 
        user_input = input("""What action would you like to complete?
    'C' for create new record.
    'R' for retrieve a record.
    'U' for update a record.
    'D' for delete a record.
    or 'EXIT' to close the program.""").lower()  
        if user_input == 'c':
            user_list = []
            print("You have selected create new record.\n")
            user_name = input("What is the name?\n")
            user_address = input("What is the address?\n")
            user_phone = input("What is the phone number?\n")
            user_email = input("What is the email?\n")
            user_age = input("What is the age?\n")
            
            user_list = [user_name, user_address, user_phone, user_email, user_age]
            values.append(user_list)
            for value in user_list:    
                user_dict = (dict(zip(keys,user_list)))
            contact_list.append(user_dict)
            formatted_list = format_to_csv(values, keys)
            #print(formatted_list)
            with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), filename), 'r+') as file:
                file.write(formatted_list)
        

            
        
        elif user_input == 'r':
            print("You selected: Retrieve a record.\n")
            user_name = input("Whose contact information do you want to see?").lower()
            not_found = True
            for element in contact_list:
                if element["name"]== user_name:
                    print(element)
                    not_found = False
                    formatted_list = format_to_csv(values, keys)
                    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), filename), 'r+') as file:
                        file.write(formatted_list)
            if not_found:
                print("Contact not found in contacts list.")


        elif user_input == 'u':
            print("You selected: Update a record. \n")
            user_name = input("Whose information would you like to update?\n").lower()
            for element in contact_list:
                if element["name"] == user_name:
                    print(element)
                    update_element = input("User found! What part of their information would you like to update?\n").lower()
                    if update_element in element.keys():
                        user_update = input(f"You want to update {element['name']}'s {update_element}? What is the update?\n")
                        element[update_element] = user_update
                        formatted_list = format_to_csv(values, keys)
                        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), filename), 'r+') as file:
                            file.write(formatted_list)
                    else:
                        print('Option not found. ')
                        pass
                else:
                    print("User not found.")
                    pass

        elif user_input == 'd':
            print("You selected delete.\n")
            user_name = input("Whose information would you like to delete?\n").lower()
            not_found = True
            for element in contact_list:
                
                if element["name"] == user_name:
                    print(f"Deleting {user_name} from your contacts list.\n")
                    values.remove(element)
                    not_found = False
                    formatted_list = format_to_csv(values, keys)
                    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), filename), 'r+') as file:
                        file.write(formatted_list)
            if not_found:
                    print("Contact not found.")


        elif user_input == 'exit':
            print("Thanks, goodbye.")
            return
        #else:
        #    print("Not a valid response.")
        #    pass
crud_loop()
