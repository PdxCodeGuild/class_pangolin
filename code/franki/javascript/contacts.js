let contactList = [{'name': 'matthew', 'favoriteFruit': 'blackberries', 'favoriteColor': 'orange'}, {'name': 'Sam', 'favoriteFruit': 'pineapple', 'favoriteColor': 'green'}, {'name': 'Al', 'facoriteFruit': 'kiwi', 'favoriteColor': 'green'}]

while (True) {
    let searchTerm = prompt("Enter the name you are looking for, or 'exit' to quit. ").toLowerCase()
    if (search_term === "exit") {
        break
    }
    else { 
        for (let i=0; i<contactList.length; i++) {
            if (contactList[i]['name'] === searchTerm) {
                let index = i;
                break
            }
        }
        
            else: 
                index = 'none'
        if index == 'none':
            user_answer = input(f"I can't find {search_term} in my list. Would you like to add an entry for {search_term}? y/n ")
            if user_answer in ['n', 'no']:
                break
            elif user_answer in ['y', 'yes']:
                new_entry = {}
                new_entry['name'] = search_term
                new_entry['favorite_fruit'] = input(f"What is {search_term}'s favorite fruit? ")
                new_entry['favorite_color'] = input(f"What is {search_term}'s favorite color? ")
                contact_list.append(new_entry)
                print(contact_list)
        else: 
            print(f"Name: {contact_list[index]['name']} \n Favorite fruit: {contact_list[index]['favorite_fruit']} \n Favorite color: {contact_list[index]['favorite_color']}")
            user_choice = input("Type 'edit' to edit this contact. Type 'delete' to delete it. Or, type 'done' to continue. ").lower()
            if user_choice == 'done':
                continue
            elif user_choice == 'delete':
                contact_list.pop(index)
                print(f"The contact for '{search_term} has been deleted.")
                print(contact_list)
            elif user_choice in ['e', 'edit']:
                while True:
                    value_choice = input("What do you want to change? Type 'name', 'fruit', 'color', or 'done' to cancel. ").lower()
                    if value_choice == 'done':
                        break
                    elif value_choice == 'name':
                        contact_list[i]['name'] = input("Enter the updated information. ")
                    elif value_choice == 'fruit':
                        contact_list[i]['favorite_fruit'] = input("Enter the updated information. ")
                    elif value_choice == 'color':
                        contact_list[i]['favorite_color'] = input("Enter the updated information. ") 
                    print(f"Here is the updated entry: \n {contact_list[i]}")
                    if input("Do you want to make another change? y/n ") == 'y':
                        continue
                    else:
                        break
    }
}
new_list = []
key_list = list(contact_list[0].keys())
new_list.append(','.join(key_list))
for i in range(len(contact_list)):
    mini_list = []
    for key in key_list:
        mini_list.append(contact_list[i][key])
    new_list.append(",".join(mini_list))
new_list = "\n".join(new_list)
print(new_list)
with open('new_contacts.csv', 'w') as file:
    file.write(new_list)
print("Bye!")