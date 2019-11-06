with open('contact_list.csv', 'r') as file:
    lines = file.read().split('\n')

contactList = []
my_dict = {}
header = []
my_line = []
new_list = []
final_list = []
final_text = []

lines = [x for x in lines if x]

for contact in lines:
    my_line = contact.split(",")
    contactList.append(my_line)

header = zip(contactList[0])

new_list = zip(contactList[1], contactList[2])

for i in range(1, len(contactList)):
    my_list = list(zip(contactList[0], contactList[i]))

    my_dict = dict(my_list)

    final_list.append(my_dict)

user_choice = ""
user_name = ""
user_fruit = ""
user_color = ""

user_choice = input(
    "Would you like to 'C'reate a new user, 'F'ind a user, 'U'pdate a user, or 'D'elete a user? ").lower()

if user_choice == "c":
    # create new user
    user_name = input("Enter a name: ")
    user_fruit = input("Enter a fruit: ")
    user_color = input("Enter a color: ")
    my_dict.update({'Name': user_name, 'Favorite Fruit': user_fruit, 'Favorite Color': user_color})
    print(f"Here is the record you just created: {my_dict}")
elif user_choice == "f":
    # do a look up .get
    user_name = input("Enter a name: ")
    # print(my_dict)
    for n in final_list:
        if n['Name'] == user_name:
            print(n)


elif user_choice == "u":
    # use the .update
    user_name = input("Enter a name: ")
    get_attrib = input("Would you like to update the 'F'ruit or the 'C'olor? ").lower()

    if get_attrib == 'f':
        user_fruit = input("Which fruit? ")
        my_dict.update({'Favorite Fruit': user_fruit})
    elif get_attrib == 'c':
        user_color = input("Which color? ")
        my_dict.update({'Favorite Color': user_color})
    for n in final_list:
        if n['Name'] == user_name:
            print(n)
elif user_choice == "d":
    # delete the record
    user_name = input("Enter a name: ")

    for n in final_list:
        if n['Name'] == user_name:
            del my_dict['Name']
            del my_dict['Favorite Fruit']
            del my_dict['Favorite Color']

    # For testing to confirm that the Name was removed
    # for n in final_list:
    #     if n['Name'] == user_name:
    #         print("User not found or deleted.")

final_text = my_dict.keys()


final_keys = []
final_keys.append(','.join(my_dict.keys()))
final_values = []
for d in final_list:
    final_values.append((','.join(d.values())))

print(final_keys)


print(final_values)
print(final_keys)
final_string = final_keys + final_values
final_string = str(final_string)


final_string = final_string.replace("['", "")
final_string = final_string.replace("']", "")
final_string = final_string.replace("', '", ", ")
final_string = final_string.replace(", ", ", \n")
print(final_string)
with open('contact_list.csv', 'w', newline="\n") as file:
    file.write(final_string)
