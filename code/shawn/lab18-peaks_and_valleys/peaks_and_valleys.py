# Shawn Stolsig
# PDX Code Guild 
# Assignment: Lab 18 - Peaks and Valleys
# Date: 10/30/2019

# function for returning indicies of peaks
def peaks(data):
    ''' Arguments: peak/valley data list Return: list of peak indicies as ints '''
    # a peak is where n is greater than both n+1 and n-1 

    # declare empty return list
    return_list = []

    # iterate through data, skip first and last element since those can't be peaks or valleys 
    # this will also help prevent IndexErrors below
    for i in range(1,len(data)-1):
        # if the element at index + 1 and index - 1 are both less than element at i
        if data[i] > data[i+1] and data[i] > data[i-1]:
            # append index of peak
            return_list.append(i)
    
    # return return list
    return return_list

# function for returning indicies of valleys
def valleys(data):
    ''' Arguments: peak/valley data list Return: list of valleys indicies as ints '''
    # a valley is where n is less both than n+1 and n-1 

    # declare empty return list
    return_list = []

    # iterate through data, skip first and last element since those can't be peaks or valleys 
    # this will also help prevent IndexErrors below
    for i in range(1,len(data)-1):
        # if the element at index + 1 and index - 1 are both greater than element at i
        if data[i] < data[i+1] and data[i] < data[i-1]:
            # append index of peak
            return_list.append(i)
    
    # return return list
    return return_list

# funcition that returns true if a peak comes first
def is_peak_first(p_list, v_list):
    return p_list[0] < v_list[0]

# function that compiles single list of peaks and valleys in order of appearance in the original data
def peaks_and_valleys(data):
    ''' Arguments: peak/valley data list Return: list of peaks/valleys in order of original input data '''

    # get peaks and valleys seperately
    peak_list = peaks(data)
    valley_list = valleys(data)

    # declare return list
    return_list = []

    # note: since we dont consider first and last index, there will always been an equal number of peaks and valleys
    #       also, they will always alternate in order


    # if peak comes first
    if is_peak_first(peak_list, valley_list):
        # iterate through peak list
        for i in range(len(peak_list)):
            # append peak then valley
            return_list.append(peak_list[i])
            return_list.append(valley_list[i])
    else:
        # iterate through peak list
        for i in range(len(peak_list)):
            # append valley then peak
            return_list.append(valley_list[i])
            return_list.append(peak_list[i])            

    return return_list

# function for returning highest value in data
def find_highest_point(data):
    ''' arguments: list of elevations as ints 
        return: highest point in elevations '''

    highest = 0
    for point in data:
        if point > highest:
            highest = point
    return highest

# function for printing 
def print_range(data):
    ''' arguments: none
        returns: how much water in range (also prints range) '''

    # counter for calculating how much water 
    water_counter = 0

    # nested for loops for printing out data.  left index is row, right index is column
    # use highest point plus two to account for the fact that 1) hight starts at 1, not 0 and 
    # 2) keep one row of sky above highest mountain
    for y in range(find_highest_point(data)+1,0,-1):

        # x will be an element in data, not an index
        for x in range(len(data)):
            # determine what to print: '  ' for air, 'X ' for ground, 'O ' for water
            # if too high and not water, print " "
            if data[x] < y and not is_water(data, x, y):
                print('   ', end='')
            # if too high and is water, print O
            elif data[x] < y and is_water(data, x, y):
                print('O  ', end='')
                water_counter += 1
            # else, must be ground so print X
            elif data[x] >= y:
                print('X  ', end='')
        print()

    # return water counter
    return water_counter

# function for figuring out if spot is in water
def is_water(data, x, y):
    ''' parameters: data and location (index) along range, and height we're evaluating
        return: returns true if water, false if not water'''

    # recursively check to left and right, if there is land return true, else return false
    is_land_to_left = check_left(data,x,y)
    is_land_to_right = check_right(data,x,y)

    # return if there is land to both left and right
    return is_land_to_left and is_land_to_right

# recursive function to check left
def check_left(data,x,y):
    # edge case: you've found the edge
    if x <= -1 or x >= len(data):
        return False        # you've found the edge
    elif data[x] == y:
        return True         # you've found land...element in data is equal to current height
    else:
        return check_left(data, x-1, y)     # call the check left function recursively, passing x-1 as the new x coordinate

# recursive function to check right
def check_right(data,x,y):
    # edge case: you've found the edge
    if x <= -1 or x >= len(data):
        return False        # you've found the edge
    elif data[x] == y:
        return True         # you've found land...element in data is equal to current height
    else:
        return check_right(data, x+1, y)     # call the check left function recursively, passing x+1 as the new x coordinate

# sample data
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
test_data_w = [11,10,9,8,7,6,5,4,5,6,7,6,5,4,5,6,7,8,9,8,7,6,5,4]
test_data_center = [5,4,3,2,1,2,3,4,5]
test_data_left = [1,2,3,4,5]
test_data_right = [5,4,3,2,1]

# main
print("Assignment Version 1: ")
print(f' peaks: {peaks(data)}, valleys: {valleys(data)}')
print(f' peaks and valleys: {peaks_and_valleys(data)}')
print("\n\nSlope to left: ")
print(f' there is {print_range(test_data_left)} water in this range')
print("\n\nSlope to right: ")
print(f' there is {print_range(test_data_right)} water in this range')
print("\n\nCenter/single valley: ")
print(f' there is {print_range(test_data_center)} water in this range')
print("\n\nAdvanced scenario...a 'W': ")
print(f' there is {print_range(test_data_w)} water in this range')
print("\n\nAssigned scenario....other data sets above:")
print(f' there is {print_range(data)} water in this range')