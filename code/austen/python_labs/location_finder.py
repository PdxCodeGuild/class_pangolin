
import webbrowser
from geopy.geocoders import Nominatim
import pandas as pd

data = pd.read_csv('climbing.csv')
key_things = data
#print (data)
#print(key_things)

things = [] 
print ('***Welcome to the destination tool***')

def export_list():
    keys = []
    values = []
    for things1 in things:
        for k, v in things1.items():
            keys.append(k)
            values.append(v)

    results = pd.DataFrame({'Places': keys, 'Location': values})
    results.to_csv("climbing.csv", index =False)

def input_stuff():
    user = [input('what is the location you would like to add to the list? ')]
    new = dict(zip(key_things,user))
    things.append(new)
    print(things)
    export_list()
   

def find():
    key = input('What is the destination you would like to see? ')
    geolocator = Nominatim()
    location = geolocator.geocode(key)
    latitude = str(location.latitude)
    longitude = str(location.longitude)
    url = "https://www.google.com/maps/@"+latitude+","+longitude+","+"18z"
    webbrowser.open_new_tab(url)

            
def delete():
    delete = input('What destination do you want to delete? ')
    for i in range(len(things)):
        if things[i]['Places'] == delete:
            del things[i]
            print(things)
            export_list()
            return things


while True:
    what_to_do = input('\nWhat would you like to do? (Create future destination, Find spot on the map, Delete your least favorite climing place?)\nenter [c, f, d] or done: ')

    if what_to_do == 'c':
        input_stuff()
    elif what_to_do == 'f':
        find()
    elif what_to_do == 'd':
        delete()
    elif what_to_do == 'done':
        break
    else:
        print(f'please enter a valid responce.')
        