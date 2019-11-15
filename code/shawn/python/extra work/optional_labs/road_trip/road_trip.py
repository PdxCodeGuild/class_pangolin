# Shawn Stolsig
# PDX Code Guild
# Assignment: Optional Lab - Road Trip
# Date: 11/4/2019

import math

# given dictionary with travel times
city_to_accessible_cities_with_travel_time = {
    'Boston': {'New York': 4, 'Albany': 6, 'Portland': 3},
    'New York': {'Boston': 4, 'Albany': 5, 'Philadelphia': 9},
    'Albany': {'Boston': 6, 'New York': 5, 'Portland': 7},
    'Portland': {'Boston': 3, 'Albany': 7},
    'Philadelphia': {'New York': 9},
}

# given dictionary with travel times
expanded_city_to_accessible_cities_with_travel_time = {
    'Boston': {'New York': 4, 'Albany': 6, 'Portland': 3},
    'New York': {'Boston': 4, 'Albany': 5, 'Philadelphia': 9},
    'Albany': {'Boston': 6, 'New York': 5, 'Portland': 7},
    'Portland': {'Boston': 3, 'Albany': 7},
    'Philadelphia': {'New York': 9, 'Washington DC': 4, 'Nashville': 7},
    'Washington DC': {'Philadelphia': 4, 'Charlotte': 4, 'Atlanta': 7},
    'Charlotte': {'Washington DC': 4, 'Atlanta': 4},
    'Nashville': {'Philadelphia': 7, 'Atlanta': 3},
    'Atlanta': {'Washington DC': 7, 'Nashville': 3, 'Charlotte': 4 }
}

# function for printing one and two hop cities
def print_one_and_two_hop_cities(cities, start):
    ''' arguments: cities dataset, start city (string)
            return: none (just prints out cities within one and two hops of start)'''

    # print cities within one hop of input cities
    print(
        f"Cities within 1 hop: of {user_input}: {get_cities_within_range(cities, start, 1)}")

    # print cities within two hop of input cities
    print(
        f"Cities within 2 hops: of {user_input}: {get_cities_within_range(cities, start, 2)}")

# function for getting list of cities in certain hop range
def get_cities_within_range(cities, start, input_range):
    ''' arguments: city data dict, start city (as string), number of hops (as int)
            return: list of all cities in given hop range (including the start city)'''

    # function for tracking cities within reach
    cities_in_range = [start]

    # continue looping while there are still available hops left
    while input_range > 0:
        # declare empty list that will be appended to cities in range
        append_list = []
        # iterate through all cities currently within range
        for city in cities_in_range:
            # add cities that are within one hop to append list
            append_list += cities[city]
        # add append list to cities in range
        cities_in_range += append_list
        # decrement range variable to account for this hop
        input_range -= 1

    # remove duplicates with list comprehension
    cities_in_range_no_dupe = []
    [cities_in_range_no_dupe.append(
        x) for x in cities_in_range if x not in cities_in_range_no_dupe]

    # return list of cities within range
    return cities_in_range_no_dupe

# function to get closest non-visted city (for Dijkstra's Algorithm)
def get_next_node(cities, min_tree, start, cities_in_range):
    ''' arguments: cities dataset, start city as a string, and cities in range as list
        return: tuple: closest city as a string, distance as int'''
    
    # initialize min to high value and city_name to track closest
    min = math.inf
    city_name = 'No more unvisited nodes'
    # iterate through city's neighboring cities
    for city in min_tree:
        # if city is closer than the current closest distance
        if min_tree[city][0] < min and min_tree[city][1] == False:
            # update current closest distance
            min = min_tree[city][0]
            # save name of closest city
            city_name = city

    # return name and distance closest city
    return city_name,min

# function to see if all cities have been visited (for Dijkstra's Algorithm)
def all_cities_visited(min_tree):
    ''' arguments: takes min_tree dict
        returns: bool if all cities are visited or not '''
    for city in min_tree:
        if min_tree[city][1] == False:
            return False
    return True

# function for getting lengths between start city and other cities in range (uses Dijkstra's Algorithm))
def get_shortest_paths(cities, start, input_range):
    ''' arguments: cities (dict of dict), start city (string), number of hops/range (int),
            return: list of paths as tuple (destination as string, shortest path length as int)'''

    # use get_cities_within_range function to find all cities in range
    cities_in_range = get_cities_within_range(cities, start, input_range)

    #  Dijkstra’s algorithm:
    # 1. Mark your selected initial node with a current distance of 0 and the rest with infinity.
    # 2. Set the non-visited node with the smallest current distance as the current node C.
    # 3. For each neighbor N of your current node C: add the current distance of C with the weight of the edge connecting C-N. If it's smaller than the current distance of N, set it as the new current distance of N.
    # 4. Mark the current node C as visited.
    # 5. If there are non-visited nodes, go to step 2.

    # 1. Mark your selected initial node with a current distance of 0 and the rest with infinity.
    # min_tree will be tree of minimum paths between start node and every othe rnode
    min_tree = {start:[0,True]}                         # index 0 is distance from start node, index 1 is True/False if node's been visited
    # for each city in cities_in_range
    for city in cities_in_range:
        if city not in min_tree.keys():
            # add key/value pair with name:inf to initialize
            min_tree[city] = [math.inf,False]

    # 2. Set the non-visited node with the smallest current distance as the current node C.
    # set current node to start
    current_node = start

    # continue to loop while there are unvisited cities
    while not all_cities_visited(min_tree):

        # for each neighbor of the current city
        for neighbor in cities[current_node]:
            # print(f"Current node is {current_node}.  Checking neighbor {neighbor}")
            # ignore visited nodes and neighbor noods that aren't in range
            if neighbor in cities_in_range and min_tree[neighbor][1] == False:

                # 3. For each neighbor N of your current node C: add the current distance of C with the weight of the edge connecting C-N. 
                #    If it's smaller than the current distance of N, set it as the new current distance of N.

                # trial sum is distance from start node to neighbor
                trial_sum = min_tree[current_node][0] + cities[current_node][neighbor]
                # print(f"Checking neightbor {neighbor}.  Neighbor is {cities[current_node][neighbor]} away from {current_node}, and {trial_sum} away from start: {start}")

                # if trial sum is less than prexisting distance value
                if min_tree[neighbor][0] > trial_sum:
                    # print(F"{neighbor} was previously {min_tree[neighbor][0]} far away from {start}.  But since {trial_sum} is less than this, updating.")

                    # update existing distance from start node to this neighbor
                    min_tree[neighbor][0] = trial_sum
                else:
                    # print(f"{neighbor} was previously {min_tree[neighbor][0]} far away from {start}.  But since {trial_sum} is >= than this, NOT updating.")
                    pass
            else:
                # print(f"ignoring neighbor {neighbor} becuase it's either out of range or has been visited already")
                pass

        # get next current node
        closest_city_name, closest_city_distance = get_next_node(cities, min_tree, current_node,cities_in_range)
        # print(f"Finding closest neighbor of {current_node}.  Closest neighbor is {closest_city_name} which is {closest_city_distance} away.")

        # 4. Mark the current node C as visited.
        min_tree[current_node][1] = True

        # 5. If there are non-visited nodes, go to step 2.
        if closest_city_name == 'No more unvisited nodes':
            break

        # assign next current node
        current_node = closest_city_name 
        # print(f'after step 3, min_tree is {min_tree}')

    # translate min_tree list into tuple to be returned
    ret_list = []
    for city in min_tree:
        ret_list.append( ( city , min_tree[city][0] )  )

    # return list of tuples
    return ret_list

# main:
## comment out one of these lines to change city map, using either given or expanded
# city_dict = city_to_accessible_cities_with_travel_time          
city_dict = expanded_city_to_accessible_cities_with_travel_time

# version 1 (show one and two hop cities)
while True:
    # get user input city
    user_input = input("Enter a city or (done) for version 2: ")
    # if city is recognized/valid
    if user_input in city_dict.keys():
        # print cities within one and two hop of input cit
        print_one_and_two_hop_cities(city_dict, user_input)
    # if user inputs 'done' go to version 2
    elif user_input in ['done', 'd', '']:
        print("On to version 2...")
        break
    else:
        print("City not found, try again.")

# version 2 (input city and num hops, return cities in range)
while True:
    # get user input for origin
    user_origin = input("Enter origin city or (done): ")
    # if origin city is recognized/valid:
    if user_origin in city_dict.keys():
            # get user input for range
        user_range = int(input("Enter number of hops: "))
        # if a valid range
        if user_range > 0:
            # print out cities within range
            within_range = get_cities_within_range(city_dict, user_origin, user_range)
            print(f"Cities in {user_range} hop(s) of {user_origin} are: {within_range}")
            # print out shortest travel time
            shortest_paths = get_shortest_paths(city_dict, user_origin, user_range)
            for path in shortest_paths:
                print(f"Shortest travel distance from {user_origin} to {path[0]} is {path[1]}")
            print(f"No other cities can be reached within {user_range} hops.")
    # advance to next version if user enters done
    elif user_origin in ['done', 'd', '']:
        break
    else:
        print("City not found, try again.")

print("Program quitting...")