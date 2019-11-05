# Shawn Stolsig
# PDX Code Guild 
# Assignment: Optional Lab - Road Trip
# Date: 11/4/2019

# given dictionary:
city_to_accessible_cities = {
  'Boston': {'New York', 'Albany', 'Portland'},
  'New York': {'Boston', 'Albany', 'Philadelphia'},
  'Albany': {'Boston', 'New York', 'Portland'},
  'Portland': {'Boston', 'Albany'},
  'Philadelphia': {'New York'}
}

# given dictionary with travel times
city_to_accessible_cities_with_travel_time = {
  'Boston': {'New York': 4, 'Albany': 6, 'Portland': 3},
  'New York': {'Boston': 4, 'Albany': 5, 'Philadelphia': 9},
  'Albany': {'Boston': 6, 'New York': 5, 'Portland': 7},
  'Portland': {'Boston': 3, 'Albany': 7},
  'Philadelphia': {'New York': 9},
}

# non-recursive function for printing one and two hop cities
def print_one_and_two_hop_cities(cities, start):
  # print cities within one hop of input cities
  print(f"Cities within 1 hop: of {user_input}: {get_cities_within_range(cities, start, 1)}")
  # print cities within two hop of input cities
  print(f"Cities within 2 hops: of {user_input}: {get_cities_within_range(cities, start, 2)}")

# function for getting list of cities in certain hop range
def get_cities_within_range(cities, start, range):

  # function for tracking cities within reach
  cities_in_range = [start]

  # continue looping while there are still available hops left
  while range > 0:
    # declare empty list that will be appended to cities in range
    append_list = []
    # iterate through all cities currently within range
    for city in cities_in_range:
      # add cities that are within one hop to append list
      append_list += cities[city]
    # add append list to cities in range
    cities_in_range += append_list
    # decrement range variable to account for this hop
    range -= 1

  # remove duplicates with list comprehension
  cities_in_range_no_dupe = []
  [cities_in_range_no_dupe.append(x) for x in cities_in_range if x not in cities_in_range_no_dupe]

  # return list of cities within range
  return cities_in_range_no_dupe

# main:
# version 1 (show one and two hop cities)
while True:
  # get user input city
  user_input = input("Enter a city or (done) for version 2: ")
  # if city is recognized/valid
  if user_input in city_to_accessible_cities.keys():
    # print cities within one and two hop of input cit
    print_one_and_two_hop_cities(city_to_accessible_cities,user_input)
  # if user inputs 'done' go to version 2    
  elif user_input in ['done','d','']:
    print("On to version 2...")
    break
  else:
    print("City not found, try again.")

# version 2 (input city and num hops, return cities in range)
while True:
  # get user input for origin
  user_origin = input("Enter origin city or (done): ")
  # if origin city is recognized/valid:
  if user_origin in city_to_accessible_cities.keys():
      # get user input for range
      user_range = int(input("Enter number of hops: "))
      # if a valid range
      if user_range > 0:
        # print out cities within range
        within_range = get_cities_within_range(city_to_accessible_cities_with_travel_time, user_origin, user_range)
        print(f"Cities in {user_range} hop(s) of {user_origin} are: {within_range}")
  # advance to next version if user enters done
  elif user_origin in ['done','d','']:
    print("On to version 2...")
    break
  else:
    print("City not found, try again.")


print("Program quitting...")














# def get_path(cities, origin, destination, path):

#   # append origin to path
#   path.append(origin)
#   print(f'Just appended origin, path is now: {path}')
#   # if you are at destination
#   if origin == destination:
#     print(f"You've reached your destination, returning path: {path}")
#     return path

#   else:
#     for city in cities[origin]:
#     # if city is in path already, do nothing...prevents going in loops
#       if city in path:
#         pass
#       else:
#         return get_path(cities, city, destination, path)


  