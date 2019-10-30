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
    for y in range(find_highest_point(data)+2,-1,-1):
        for x in data:
            # determine what to print: '  ' for air, 'X ' for ground, 'O ' for water
            # if too high, print air
            if x <= y and not is_water(data, x, y):
                print('   ', end='')
            elif x <= y and is_water(data, x, y):
                print('O  ', end='')
                water_counter += 1
            elif x > y:
                print('X  ', end='')

        print()

    # return nothing
    return water_counter

# function for figuring out if spot is in water
def is_water(data, x, y):
    ''' parameters: data and location (index) along range, and height we're evaluating
        return: returns true if water, false if not '''

    # if you can find land (an int of equal value to y the left and to the right x), then return true
    is_land_to_left = False
    is_land_to_right = False

    # iterate left: from current x location to 1, -1 increment at a time
    for i in range(x,0, -1):
        if data[i] == y:
            is_land_to_left = True
            break                       # exit loop once land is found

    # iterate right: from current x location to len(data), +1 increment at a time
    for i in range(x,len(data), 1):
        if data[i] == y:
            is_land_to_left = True
            break                       # exit loop once land is found

    # return if there is land to both left and right
    return is_land_to_left and is_land_to_right


# sample data
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
#ind = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20]

# main
print(f' peaks: {peaks(data)}, valleys: {valleys(data)}')
print(f' peaks and valleys: {peaks_and_valleys(data)}')
print(f' there is {print_range(data)} water in this range')