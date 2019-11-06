'''
Lab 23: Contact List - Version 3

Purpose/goal: When REPL loop finishes:
    
    - Write the updated contact info to the CSV file to be saved. - D
    
    - Save a backup contacts.csv because you likely won't write it correctly the first time. - D
'''

# open contacts.csv
with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')

    # make lists lowercase
    lines = [line.lower() for line in lines]
    
    # replace " " with "_"
    lines = [line.replace(" ", "_") for line in lines]
    
    # remove redundant ","s
    lines = [line.replace(",,,,", "") for line in lines]
    
    # remove extra "''"
    trash = lines.pop()
    
    # isolate / assign keys: values in dicts
    keys = lines[0].split(",")
    
    # remove keys from lines
    lines.pop(0)

    # create values_list
    values_list = []
    for line in lines:
        values_list.append(line.split(","))
    
    # create dicts list
    contact_list_dicts = []

    # put list items into dict
    for values in values_list:
        contact_list_dicts.append({keys[0]: values[0], keys[1]: values[1], keys[2]: values[2]})

# invite user to CRUD    
user_op = input("Hello! Would you like to create, retrieve, update or delete a record? ").lower()

# create options list
op_list = ["create", "retrieve", "update", "delete", ""]

# create while loop to catch unrelated answers
while user_op not in op_list:
    user_op = input("Please select one from these options - create, retrieve, update or delete: ").lower()
    if user_op in op_list:
        break

# user creates
if user_op == "create":
    create = [input("Great! Please enter the contact's name, favorite fruit & favorite color: " ).lower()]
    for entry in create:
        values_list.append(entry.split(","))
    for values in values_list:
        contact_list_dicts.append({keys[0]: values[0], keys[1]: values[1], keys[2]: values[2]})
    print(contact_list_dicts)

# user retrieves
if user_op == "retrieve":
    retrieve = input("Okay. Enter the name of the contact you'd like to retrieve information about: ").lower()
    for person in contact_list_dicts:
        if retrieve == person['name']:
            print(person)

# user updates
if user_op == "update":
    name = input("Okay. Enter the name of the contact you'd like to update: ").lower()
    for person in contact_list_dicts:
        if name == person['name']:
            print(f"\nHere is {name}'s current info:\n", person, "\n")
            update_ops = "name", "favorite_fruit", "favorite_color"
            up_data = input("What would you like to update? (name, favorite fruit or favorite color): ").lower()
            up_data = up_data.replace(" ", "_")
            if up_data in update_ops:
                new_entry = input("What is the updated data? ").lower()
                person[up_data] = new_entry 
                print(f"\nPerfect! Here is {name}'s updated info:\n", person, "\n")

# user deletes
if user_op == "delete":
    delete = input("Okay. Enter the name of the contact you'd like to delete: ").lower()
    for person in contact_list_dicts:
        if delete == person['name']:
            contact_list_dicts.remove(person)
            print(f"\nGreat! Here is the updated contact list:\n\n",  contact_list_dicts, "\n")

# quit opportunity
if user_op == "":
    quit()

# format contacts_list_dicts as csv
for dicts in contact_list_dicts:
    keys = [d.replace("{", "") for d in dicts]

csv = []
csv.append(",".join(keys))

for i in range(len(contact_list_dicts)):
    values = []
    for key in keys:
        values.append(contact_list_dicts[i][key])
    csv.append(",".join(values))

csv = "\n".join(csv)

# save updated csv
with open('contacts.csv', 'w') as file:
    file.write(csv)