
with open('contact_list.csv', 'r') as file:
    lines = file.read().split('\n')
    #print(lines)

contactList = []
my_dict = {}

for contact in lines:
    print(contact)


