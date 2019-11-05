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

inp_val1 = ("y","n")

ld_to_csv = []

with open('contacts.csv', 'r') as f:
    csv_orig = f.read().split('\n')
    print(csv_orig)

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

contacts = get_dict(csv_orig)

def list_to_csv(dictList):
    ll = list(dictList[0].keys())
    dd = ','.join(ll)
    ld_to_csv.append(dd)
    for i in range(len(dictList)):
        v = list(dictList[i].values())
        vv = ','.join(v)
        ld_to_csv.append(vv)

    return ld_to_csv

# Create a record
def new_rcd(nme, frt, clr):
    new_dct = {
        'name': nme,
        'fruit': frt,
        'color': clr
    }
    return contacts.append(new_dct)

# Retrieve a record
def fnd_rcd(nme):
    for i in range(len(contacts)):
        for j in contacts[i].items():
            if contacts[i]['name'] == nme:
                j = contacts[i]
                return j
               
# Delete a record
def del_rcd(nme):
    for i in range(len(contacts)):
        if contacts[i]['name'] == nme:
                contacts.remove(contacts[i])
                return contacts

# Update a record
def upd_rcd(fnd, atr, val):
    fnd[atr] = val
    upd_rcd = fnd
    del_rcd(fnd['name'])
    contacts.append(upd_rcd)
    return contacts

def usr_inp(msg, emsg, *args):
     while True:
          usr_inp = input(msg).lower()
          if usr_inp.lower() not in args:
               print(f"\n{emsg}")
          else:
               return usr_inp

# Create a new contact loop
new_contact = usr_inp(msg1, emsg1, *inp_val1)
if new_contact == 'y':
    new_rcd(input(msg5),input(msg6),input(msg7))
 

# Retreive a contact loop
retrieve_contact = usr_inp(msg2, emsg1, *inp_val1)
if retrieve_contact == 'y':
    record = fnd_rcd(input(msg5))
    if record == None:
        print(emsg2)
    else:
        print(record)

# Update a contact loop
update_contact = usr_inp(msg3, emsg1, *inp_val1)
if update_contact == 'y':
    record = fnd_rcd(input(msg5))
    if record == None:
        print(emsg2)
    else:
        upd_rcd(record, input(msg8), input(msg9))

# Delete a contact loop
delete_contact = usr_inp(msg4, emsg1, *inp_val1)
if delete_contact == 'y':
    record = fnd_rcd(input(msg5))
    if record == None:
        print(emsg2)
    else:
        del_rcd(record['name'])


final = list_to_csv(contacts)

with open('contacts.csv', 'w') as f:
    for i in range(len(final)):
        f.write(final[i] + '\n')

