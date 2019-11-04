with open('contact_list.csv', 'r') as file:
    lines = file.read().split('\n')
    # print(lines)

contactList = []
my_dict = {}
header = []
name = []
fruit = []
color = []
my_line = []
new_list = []

for contact in lines:
    my_line = contact.split(",")
    contactList.append(my_line)

header = zip(contactList[0])
new_list = zip(contactList[1], contactList[2])

keys = list(header)
values = list(new_list)

print(keys)
print(values)
#print(my_dict)
