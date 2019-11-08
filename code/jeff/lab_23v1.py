# lab_23.py v1
# CSV
# Jeff Smith
from os.path import dirname, abspath, join
contacts_csv = join(dirname(abspath(__file__)), 'contacts.csv')
with open(contacts_csv, 'r') as file:
    lines = file.read().split('\n')
    keys = lines[0].split(',')
contact_list = []
if lines[-1] == '':
    lines.pop(-1)
# Create empty list
for line in lines[1:]:
    values = line.split(',')
    contact_list.append(dict(zip(keys, values))) # Add dictionary to list

print(contact_list)