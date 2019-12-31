'''
Lab 23: Contact List - Version 1

Purpose/goal: Build a program to manage a list of contacts. 

    - To start, we'll build a CSV ('comma separated values') together, and go over how to load that file. - D
    
    - Headers: name, favorite fruit, favorite color. Open the CSV, - D
    
    - Convert the lines of text into a list of dictionaries, one dictionary for each user. - D
    
    - The text in the header represents the keys, the text in the other lines represent the values. - D

'''

# open contacts.csv
with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')

    # make lists lowercase
    lines = [line.lower() for line in lines]
    
    # replace " " with "_"
    lines = [line.replace(" ", "_") for line in lines]
    
    # remove redundant ","s
    lines = [line.replace(",,,,", "") for line in lines]
    
    # remove extra "''"
    trash = lines.pop()
    
    # isolate / assign keys: values in dicts
    keys = lines[0].split(",")
    
    # remove keys from lines
    lines.pop(0)

    # create values_list
    values_list = []
    for line in lines:
        values_list.append(line.split(","))
    
    # create dicts list
    contact_list_dicts = []

    # put list items into dict
    for values in values_list:
        contact_list_dicts.append({keys[0]: values[0], keys[1]: values[1], keys[2]: values[2]})
    
print(contact_list_dicts)