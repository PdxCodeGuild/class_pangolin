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



# sample data
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
#ind = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20]

# main
print(f' peaks: {peaks(data)}, valleys: {valleys(data)}')
print(f' peaks and valleys: {peaks_and_valleys(data)}')
