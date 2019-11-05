'''
lab 23 version 1
written by Rhornberger
last updated nov 4 2019
'''
# acquire the info from the csv file
with open('contacts.csv', 'r') as my_file:
    #start doing something with the info
    lines = my_file.read().split('\n')
    keys = lines[0]
    keys = keys.split(',')
    list_of_contacts = []
    row = lines[1:]
    # turn the info into individual dictionaries then put those dicts into a list
    for value_str in row:
        value_list = value_str.split(',')
        contacts = {}
        for i in range(len(keys)):
            contacts[keys[i]] = value_list[i]
        list_of_contacts.append(contacts) 
    # accept user info
    new_name = input('Please enter the name of your new contact: ').lower()
    new_address = input('Please enter the address of your new contact: ').lower()
    new_phone_num = input('Please enter the phone number of your new contact: ').lower()
    new_fruit = input('Please enter the favorite fruit of your new contact: ').lower()
    new_list = (new_name, new_address, new_phone_num, new_fruit)
    #list_of_contacts2 = []
    for value in new_list:
        value_list2 = value.split(',')
        print(value_list2)
        contacts = {}
        #new_contact = zip(keys, value_list)
        #print(new_contact)
        for i in range(len(keys)):
            contacts[keys[i]] = value_list2[i]
        list_of_contacts.append(contacts)
    
print(new_list)
print(list_of_contacts)