with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    # print(lines)

contacts = []
list_of_lists = []

for line in lines:
    line = line.split(",")
    list_of_lists.append(line) 
keys = list_of_lists.pop(0)

for i in range(len(list_of_lists)):
    row = list_of_lists[i]
    contact = dict(zip(keys, row))
    contacts.append(contact)

def create_record():
    name = input("Enter a name:  ")
    fruit = input("Enter favorite fruit:  ")
    color = input("Enter favorite color:  ")
    row = name ,fruit, color
    contact = dict(zip(keys, list(row)))
    contacts.append(contact)
    return contacts

def retrieve_record():
    find_name = input("Enter the name of the contact:  ")  
    for contact in contacts:
        if contact.get("Name") == find_name:
            return contact

def update_record():
    find_name = input("Enter the name of the contact:  ") 
    for contact in contacts:
        if contact.get("Name") == find_name:
            contact_dict = contact
        change_value = input("What value would you like to change?  Name, favorite fruit, or favorite color?  Type 'name', 'fruit', 'color', or 'done':  " )
        if change_value == "name":
            new_name = input("What would you like to change the name to?  ")
            contact_dict["Name"] = new_name
        elif change_value == "fruit":
            new_fruit = input("What would you like to change the favorite fruit to?  ")
            contact_dict["Favorite Fruit"] = new_fruit
        elif change_value == "color":
            new_color = input("What would you like to change the color to?  ")
            contact_dict["Favorite Color"] = new_color
        else:
            break    
    return contacts

def delete_record():
    name = input("What is the name of the contact you would like to delete?  ") 
    for i in range(len(contacts)-1):
        if contacts[i]["Name"] == name:
            del contacts[i]
    return contacts

def main():
    while True:
        action = input("What would you like to do?  View all contacts, create new, view by name, update, or delete a record?  Enter 'all', 'new', 'by name', 'update', 'delete', or 'done' to exit:  ")
        if action == "all":
            print(contacts)
        elif action == "new":
            print(create_record())
        elif action == "by name":
            print(retrieve_record())     
        elif action == "update":
            print(update_record())
        elif action == "delete":
            print(delete_record())    
        else:
            break    
main()