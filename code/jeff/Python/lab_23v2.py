# lab_23.py v1
# CSV
# Jeff Smith
from os.path import dirname, abspath, join

contacts_csv = join(dirname(abspath(__file__)), 'contacts.csv')

with open(contacts_csv, 'r') as file:
    lines = file.read().split('\n')
    keys = lines[0].split(',')
    contact_list = []
    
    if lines[-1] == '':
        lines.pop(-1)
    
    # Create empty list
    for line in lines[1:]:
        values = line.split(',')
        contact_list.append(dict(zip(keys, values))) # Add dictionary to list

'''Version 2 - Implement a CRUD REPL
*Create a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.'''
newcon = {}
new_name = input('Enter a name for the new contact: ',)
new_addr = input('Enter the new address: ',)
new_phone = input('Enter the new phone: ',)
new_fruit = input('Enter the new favorite fruit: ',)
new_color = input('Enter the new color: ',)

contact_list.append({'Name': new_name, 'Address': new_addr, 'Phone Number': new_phone, 'Favorite Fruit': new_fruit, 'Favorite Color': new_color})

print(contact_list)

def retrieve():
    '''Retrieve a record:'''
    select = input('Who would you like to review? ').lower()
    display = []
    for entry in contact_list:
        if entry['Name'].lower().find(select) >= 0:
            display.append(entry)
    print(display)     
retrieve()

    #'''Update a record: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.'''

def modify():
    '''Retrieve a record:'''
    select = input('Who would you like to change? ').lower()
    update = input('Which section would you like to update? ').lower()
    change = input('What is the new information? ').lower()

    for entry in contact_list:
        if entry['Name'].lower().find(select) >= 0:
            for key in entry.keys():
                if key.lower() == update:
                    entry[key] = change

    for entry in contact_list:
        if entry['Name'].lower().find(select) >= 0:
            print(entry)

modify()

'''Delete a record: ask the user for the contact's name, remove the contact with the given name from the contact list.'''

def delcon():
    #Delete a contact
    select = input('Who would you like to delete? ').lower
    for i in range(len(contact_list)): 
        if contact_list[i]['Name'].lower == select: 
            del contact_list[i] 
        print(contact_list)

delcon()

'''
def create_contact(data, keys):
    new_contact = {}
    for key in keys:
        new_contact[key] = input('What is your new contact's {key}? ')
    data.append(new_contact)

def read_contact(data, keys):
    contact_input = input('Who would you like to search for? ')
    data_results = list(filter(lambda contact: contact['name'] == contact_input, data)) # Lookup lambda
    print(data_results)
    for result in data_results:
        for key, value in result.items():
            print(f'{key}: {value}')
        print('')

def update_contact(data, keys):
    contact_input = input('Who would you like to update? ')
    data_results = list(filter(lambda contact: contact['name'] == contact_input, data)) # Lookup lambda
    print(data_results)
    for result in data_results:
        for key, value in result.items():
            print(f'{key}: {value}')
        print('')
    index_to_update = input('Which entry do you want to update? ')
    data_results[index_to_update][key_to_update] = value_to_update

def delete_contact(data, keys):
    delete_contact = {}
    for key in keys:
        new_contact[key] = input('What is your new contact's {key}? ')
    data.append(new_contact)


data_csv_output = []
data_csv_output.append(list(data[0].keys()))
for contact in data:
    data_csv_output.append(list(contact.values()))
data_csv_output = [",".join(line) for line in data_csv_output]
data_csv_output = "\n".join(data_csv_output)
with open('contacts.csv', 'w') as f:
    f.write(data_csv_output)



while True:
    user_input = input('(c)reate, (r)ead, (u)pdate, (d)elete, (q)uit?')
    if user_input == 'q':
        break
    elif user_input == 'c':
        create_contact(data, keys)
    elif user_input == 'r':
        read_contact(data, keys)
    elif user_input == 'u':
        update_contact(data, keys)
    elif user_input == 'd':
        delete_user(data, keys)

'''pprint.pprint(data)