contact_list = []
with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    lines = list(lines)
    keys = lines[0].split(',')
# iterate through the lines
# split each line
# iterate through the list and assign each value to a key
# name,favorite fruit,favorite color

contact_list = []
for i in range(1, len(lines)):
    dict = {}
    values = lines[i].split(',')
    for j in range(len(values)):
        key = keys[j] 
        dict[key] = values[j]
    contact_list.append(dict)
print(contact_list)
        
      
        