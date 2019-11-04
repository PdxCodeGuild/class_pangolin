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
# print(lines)

for contact in lines:
    my_line = contact.split(",")
    contactList.append(my_line)

header = zip(contactList[0])

new_list = zip(contactList[1], contactList[2])

for i in range(1, len(contactList)):
    my_list = list(zip(contactList[0], contactList[i]))
    # print(my_list)
    my_dict = dict(my_list)
    # print(my_dict)
    final_list.append(my_dict)

# print(final_list)
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
    #print(my_dict)
    for n in final_list:
        if n['Name'] == user_name:
            print(n)
# elif user_choice == "u":
#     #use the .update
# elif user_choice == "d":
#     #delete the record


# print(my_dict)
# print(final_list)
