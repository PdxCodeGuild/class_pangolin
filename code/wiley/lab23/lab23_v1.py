#Contact List lab23
#11/4/19
#Open the CSV, convert the lines of text into a list of dictionaries, on dictionary for each user.
#The text in the header represents the keys, the text in the other lines represents the values.
import os
filename = "contacts.csv"
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), filename), 'r') as file:
    lines = file.read().split('\n')
    #print(lines)

#Make a list of keys from the first list in lines(the header)
contact_list = []
keys = lines[0].split(',')
#make a list of values
values = [x.split(',') for x in lines[1:]]

for value in values:
    #print(value)
    contact_list.append(dict(zip(keys, value)))






    
