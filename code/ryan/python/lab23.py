with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    print(lines)

contacts = []
list_of_lists = []

for line in lines:
    line = line.split(",")
    list_of_lists.append(line) 
keys = list_of_lists.pop(0)

for i in range(len(list_of_lists)):
    row = list_of_lists[i]
    contact = dict(zip(keys, row))
    contacts.append(contact)

print(contacts)
    