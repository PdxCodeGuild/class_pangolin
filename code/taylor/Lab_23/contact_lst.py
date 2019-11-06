# Taylor Rebbe 
# Lab_23
# 11/06/19

# Message variables
msg1 = "Create a contact? (y , n): > "
msg2 = "Find a contact? (y , n): > "
msg3 = "Update a contact? (y , n): > "
msg4 = "Delete a contact? (y , n): > "
msg5 = "Enter a name: > "
msg6 = "Enter a fruit: > "
msg7 = "Enter a color: > "
msg8 = "Enter name, fruit or color: > "
msg9 = "Enter a value: > "

emsg1 = "Check your input"
emsg2 = "Contact not found"

# Input validation variables
inp_val1 = ("y", "n")

# Initiated the list dictionary to csv list for writing
ld_to_csv = []

# Opens and reads a csv
with open('contacts.csv', 'r') as f:
    csv_orig = f.read().split('\n')
print(csv_orig)

# List to dictionary
def get_dict(csvL):
    """ This function takes a csv list, and uses index 0 as the "key". Key value pairs are then 
    created with the remaining range of the csv-list. the list is then converted to a list of dictionaries"""
    csv_lst = []
    csv_dct = []
    k = csvL[0].split(',')
    for i in range(1,len(csvL)):
        v = csvL[i].split(',')
        for i in range(len(k)):
            csv_dct.append((k[i], v[i]))
        csv_lst.append(dict(csv_dct))
    return csv_lst

contacts = get_dict(csv_orig)

def list_to_csv(dictList):
    """ This function creates csv list out of a list of dictionaries. The dict keys become the first line in the csv output
    and the subsequent associated values are then new indexes of a list."""
    ld_to_csv.append(','.join(list(dictList[0].keys())))
    for i in range(len(dictList)):
        ld_to_csv.append(','.join(list(dictList[i].values())))
    return ld_to_csv

# Create a record
def new_rcd(nme, frt, clr):
    """ This function creates a new dictionary to record the details of a contact. """
    new_dct = {
        'name': nme,
        'fruit': frt,
        'color': clr
    }
    return contacts.append(new_dct)

# Retrieve a record
def fnd_rcd(nme):
    """ This function searches and returns a record in a list of dictionaries"""
    for i in range(len(contacts)):
        for j in contacts[i].items():
            if contacts[i]['name'] == nme:
                j = contacts[i]
                return j
               
# Delete a record
def del_rcd(nme):
    """ This funciton removes a record from a list of dictionaries"""
    for i in range(len(contacts)):
        if contacts[i]['name'] == nme:
                contacts.remove(contacts[i])
                return contacts

# Update a record
def upd_rcd(fnd, atr, val):
    """This function receives the input form the find() function, an attribute input and a validation list to update a dictionary
    in a list of dictionaries."""
    fnd[atr] = val
    upd_rcd = fnd
    del_rcd(fnd['name'])
    contacts.append(upd_rcd)
    return contacts

def usr_inp(msg, emsg, *args):
    """This function validates user input."""
     while True:
          usr_inp = input(msg).lower()
          if usr_inp.lower() not in args:
               print(f"\n{emsg}")
          else:
               return usr_inp

# Create a new contact loop
new_contact = 'y'
while new_contact == 'y':
    new_contact = usr_inp(msg1, emsg1, *inp_val1)
    if new_contact == 'n':
        break
    if new_contact == 'y':
        new_rcd(input(msg5),input(msg6),input(msg7))
 
# Retreive a contact loop
retrieve_contact = 'y'
while retrieve_contact == 'y':
    retrieve_contact = usr_inp(msg2, emsg1, *inp_val1)
    if retrieve_contact == 'n':
        break
    else:
        record = fnd_rcd(input(msg5))
        if record == None:
            print(emsg2)
        else:
            print(record)

# Update a contact loop
update_contact = 'y'
while update_contact == 'y':
    update_contact = usr_inp(msg3, emsg1, *inp_val1)
    if update_contact == 'n':
        break
    else:
        record = fnd_rcd(input(msg5))
        if record == None:
            print(emsg2)
        else:
            upd_rcd(record, input(msg8), input(msg9))

# Delete a contact loop
delete_contact = 'y'
while delete_contact == 'y':
    delete_contact = usr_inp(msg4, emsg1, *inp_val1)
    if delete_contact == 'n':
        break
    else:
        record = fnd_rcd(input(msg5))
        if record == None:
            print(emsg2)
        else:
            del_rcd(record['name'])

final = list_to_csv(contacts)

# Opens the csv list and wirtes the updates to the csv
with open('contacts.csv', 'w') as f:
    for i in range(len(final)):
        f.write(final[i] + '\n')