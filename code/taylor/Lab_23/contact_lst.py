msg1 = "Create a contact? (Y , N): > "
msg2 = "Find a contact? (Y , N): > "
msg3 = "Update a contact? (Y , N): > "
msg4 = "Delete a contact? (Y , N): > "

msg5 = "Enter a name: > "
msg6 = "Enter a fruit: > "
msg7 = "Enter a color: > "

with open('contacts.csv', 'r') as f:
    csv_org = f.read().split('\n')

# List to dictionary
def get_dict(csvL):
    csv_lst = []
    csv_dct = []
    k = csvL[0].split(',')
    for i in range(1,len(csvL)):
        v = csvL[i].split(',')
        for i in range(len(k)):
            csv_dct.append( (k[i], v[i]) )
        csv_lst.append(dict(csv_dct))
    return csv_lst

contacts = get_dict(csv_org)

# Create a record
def new_rcd(nme, frt, clr):
    new_dct = {
        'Name': nme,
        'Fruit': frt,
        'Color': clr
    }
    return contacts.append(new_dct)

new_rcd('Tommy', 'orange', 'purple')
print(contacts)

# Retrieve a record
def fnd_rcd(nme):
    for i in range(len(contacts)):
        for j in contacts[i].items():
            if contacts[i]['Name'] == nme:
                j = contacts[i]
                return j
               
print(fnd_rcd('Jim'))

# Delete a record
def del_rcd(nme):
    for i in range(len(contacts)):
        if contacts[i]['Name'] == nme:
                contacts.remove(contacts[i])
                return contacts
               
print(del_rcd('Jim'))

# Update a record
def upd_rcd(fnd, atr, val):
    fnd[atr] = val
    upd_rcd = fnd
    del_rcd(fnd)
    contacts.append(upd_rcd)
    return contacts

print(upd_rcd(fnd_rcd('Taylor'), 'Name', 'Jimmy John'))

