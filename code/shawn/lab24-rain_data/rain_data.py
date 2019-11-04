# Shawn Stolsig
# PDX Code Guild 
# Assignment: Lab 24 - Rain Data
# Date: 11/1/2019

# function for opening file and getting input list of string lines
def open_file(filename):
    ''' arguments: filename
        returns: header list and data as a tuple '''

    with open(filename,'r') as f:
        lines = f.read().split('\n')

    # return tuple (header,data)                    ### pick up here, trying to format header/data returns.  do i even need a header?
    header = lines[9:10:][0].strip()
    data = lines[10::]
    return header,data

# main

# open file
filename = 'sample_rain_data.txt'
header,data = open_file(filename)
print(header)

# trim off header