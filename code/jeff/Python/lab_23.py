# lab_23.py
# Contact List
# Jeff Smith

contacts = {}
with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    keys = lines[0].split(',')
print(keys)

for line in lines[1:]:
    values = line.split(',')
print(list(zip(keys, values)))

for line in lines[1:]:
    values = line.split(',')

print(dict(zip(keys, values)))
contact_list = []


contact_list.append(dict(zip(keys, values)))
print(contact_list)
####################################
'''Version 2 - Implement a CRUD REPL

    *Create a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.'''
newcon = {}

new_name = input('Enter a name for the new contact: ',)
new_addr = input('Enter the new address: ',)
new_phone = input('Enter the new phone: ',)
new_fruit = input('Enter the new favorite fruit: ',)
new_color = input('Enter the new color: ',)

contacts.update([('Name', new_name), ('Address', new_addr), ('Phone Number', new_phone), ('Favorite Fruit' , new_fruit), ('Favorite Color' , new_color)])

# contacts.append({'Name': newcon, 'Address': new_addr, 'Phone Number': new_phone, 'Favorite Fruit': new_fruit, 'Favorite Color': new_color})

print(contacts)
    # *Retrieve a record: ask the user for the contact name, find the user with the given name, and display their information
    # *Update a record: ask the user for the contact name, then for which attribute of the user they want to update and the value of the attribute they want to set.
    # *Delete a record: ask the user for the contact name, remove the contact with the given name from the contact list.'''
    