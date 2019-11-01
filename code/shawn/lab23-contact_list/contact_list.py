# Shawn Stolsig
# PDX Code Guild 
# Assignment: Lab 23 - Contact List
# Date: 11/1/2019


# open file
with open('lab23_spreadsheet.csv', 'r') as file:
    # load each line into list of strings call 'lines'
    lines = file.read().split('\n')

# initialize empty list of dictionaries
dict_list = []

# use headers to initialize 
headers = lines[0].split(',')

# iterate through remaining lines in file
for line_num in range(1,len(lines)):
    # split line on comma
    this_line = lines[line_num].split(',')

    # list to hold tuples
    tup_list = []

    # print(f'headers is: {headers} and this_line is {this_line}')

    # iterate through each column header
    for col in range(len(headers)): 
        # append a dictionary with each header
        tup_list.append( (headers[col], this_line[col]) )

    # append tuple as a dict to dict list
    dict_list.append(dict(tup_list))

# print final dict
print(dict_list)