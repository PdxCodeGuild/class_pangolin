with open('contact_list.csv', 'r') as file:
    lines = file.read().split('\n')
    # print(lines)

contactList = []
my_dict = {}

for contact in lines:
    my_line = contact.split(",")
    print(my_line)

    #print(contact)

#print(name, fruit, color)
