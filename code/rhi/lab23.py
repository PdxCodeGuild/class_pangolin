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
    def add_contact():
        new_name = input('Please enter the name of your new contact: ').lower()
        new_address = input('Please enter the address of your new contact: ').lower()
        new_phone_num = input('Please enter the phone number of your new contact: ').lower()
        new_fruit = input('Please enter the favorite fruit of your new contact: ').lower()
        new_list = (new_name, new_address, new_phone_num, new_fruit)
        contacts = {}
        for i in range(len(keys)):
            contacts[keys[i]] = new_list[i]
        list_of_contacts.append(contacts)
        print('contact added', contacts)

    # ask the user who in their contacts list they want to look up
    def look_up():
        user_choice = input('What is the name of the person whos info you would like to see?: ').lower()
        #def search(name):
        contact1 = []
        for c in list_of_contacts:
            if c['name'].lower().find(user_choice) >= 0:
                contact1.append(c)
        print(contact1)  

    # give the option to update a current contact
    def update():
        user_name = input('What contact would you like to change info on?: ').lower()
        user_key = input('What info would you like to change? Please enter address, phone number, or favorite fruit: ').lower()
        user_change = input('what would you like to change information to?: ').lower()
        for c in list_of_contacts:
            if c['name'].lower().find(user_name) >= 0:
                for key in c.keys():
                    if key == user_key:
                        c[key] = user_change
        for c in list_of_contacts:
            if c['name'].lower().find(user_name) >= 0:
                print(c)

    #print(list_of_contacts)

    #delete a peice of contact info
    def delete_peice():
        user_n = input('What contact would you like to modify?: ').lower()
        user_k = input('What info would you like to modify? Please enter address, phone number, or favorite fruit: ').lower()
        for c in list_of_contacts:
            if c['name'].lower().find(user_n) >= 0:
                for key in list(c.keys()):
                    if key == user_k:
                        c.pop(key)
        # for c in list_of_contacts:
        #     if c['name'].lower().find(user_n) >= 0:
                print(list_of_contacts)
    #delete a contact
    def remove_contact():
        user_n = input('Please enter the name of the contact you want to remove from your list: ')
        for c in range(len(list_of_contacts)):
            if list_of_contacts[c]['name'].lower().find(user_n) >= 0:
                list_of_contacts.pop(c)
        print(list_of_contacts)
    # return all new info to the csv
    def csv():
        line = [[line for line in d.keys()] for d in list_of_contacts]
        lines = [line[0]] + [[lines for lines in d.values()] for d in list_of_contacts]
        print(lines)
        lines2 = []
        for line in lines:
            lines2.append(','.join(line))
        lines2 = '\n'.join(lines2)
        print(lines2)
        fl = open('contacts.csv', 'w') 
        #fl.write(lines)
        #for li in lines:
        fl.write(lines2)
        fl.close()
# start loop for asking user what they want to do with their list of contacts

user_input = input('Here at Contact Organizer we want you to have an easy time managing the info for your contact list.\n Please read the options carefully as the options may have changed.\n To see your current contact list please enter "cc": \n To add a new contact please enter "a": \n To see the information for a particular contact please enter "i": \n To update information on a contact please enter "u": \n To delete information on a contact please enter "d": \n To delete an entire contact please enter "dc": \n Please make your selection now: ').lower()
if user_input == 'cc':
    print(list_of_contacts)
elif user_input == 'a':
    add_contact()
elif user_input == 'i':
    look_up()
elif user_input == 'u':
    update()
elif user_input == 'd':
    delete_peice()
elif user_input == 'dc':
    remove_contact()
print(list_of_contacts)
option = input('Would you like to make these changes permanent? Please enter "y" for yes and "n" for no: ').lower()
if option == 'y':
    csv()
else:
    print('Thank you for using Contact Organizer. We hope that your experience was pleasent and that you will come see us again!')

    