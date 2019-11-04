with open('contact_list.csv', 'r') as file:
    lines = file.read().split('\n')
    # print(lines)

contactList = []
my_dict = {}
header = []
# name = []
# fruit = []
# color = []
my_line = []
new_list = []
final_list = []

lines = [x for x in lines if x]
#print(lines)

for contact in lines:
    my_line = contact.split(",")
    contactList.append(my_line)

header = zip(contactList[0])

new_list = zip(contactList[1], contactList[2])


for i in range(1, len(contactList)):
    my_list = list(zip(contactList[0], contactList[i]))
    #print(my_list)
    my_dict = dict(my_list)
    #print(my_dict)
    final_list.append(my_dict)

print(final_list)