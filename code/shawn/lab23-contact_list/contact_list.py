# Shawn Stolsig
# PDX Code Guild 
# Assignment: Lab 23 - Contact List
# Date: 11/1/2019

# function for opening file
def open_file(filename):
    ''' arguments: filename to open
        return: list of each line as a string '''
    # open file
    with open(filename, 'r') as file:
        # load each line into list of strings call 'lines'
        lines_string = file.read().strip()      # removes whitespace and newlines
        lines = lines_string.split('\n')
    
    return lines

# function for writing data to file
def write(filename, output_string):
    ''' arguments: filename to output to and string to write
        returns: boolean if operation was successful '''

    try: 
        with open(filename, 'w') as file:
            file.write(output_string)
        return True
    except IOError as e:
        print(e)
        return False

# function to convert list of comma seperated lines to a dictionary
def get_dictionary(input_string_list):
    ''' arguments: input list of strings.  each string is a line with comma seperated values,
        return: dictionary with the first line/headers as keys '''

    # initialize empty list of dictionaries
    dict_list = []

    # use headers to initialize 
    headers = input_string_list[0].split(',')

    # iterate through remaining lines in file
    for line_num in range(1,len(input_string_list)):
        # split line on comma
        this_line = input_string_list[line_num].split(',')

        # list to hold tuples
        tup_list = []

        # iterate through each column header
        for col in range(len(headers)): 
            # append a dictionary with each header
            tup_list.append( (headers[col], this_line[col]) )

        # append tuple as a dict to dict list
        dict_list.append(dict(tup_list))

    # return list of dictionaries
    return dict_list

# function to create dictionary input
def create(headers):
    ''' arguments: list of headers,
        returns: a dictionary of header/value pairs'''

    # declare list for holding inputs
    new_entry_list = []

    # get input.  iterate through headers, get string for each one
    for i in range(len(headers)):
        # append input to list
        new_entry_list.append(input(f"Please input {headers[i]}: "))

    # tuple list for later converting to dictionary
    tup_list = []

    # use header and new entry list to create tuple, which will be converted to a dictionary
    for i in range(len(new_entry_list)):
        # append header/value pair to tuple list
        tup_list.append(  (headers[i],new_entry_list[i])  )

    # cast tuple to a dictionary and return
    return dict(tup_list)

# function to retrieve/dispay info
def retrieve(dict_list, lookup):
    ''' arguments: the list of dictionaries and the column label that'll be used to lookup 
        returns: string of lookup values'''

    user_input = input(f"Please input what {lookup} you'd like data for: ")

    # iterate through dictionary list
    for entry in dict_list:
        # if name matches input
        if entry[lookup] == user_input:
            # return current element
            return entry

    # return none if not found
    return None

# function to update data in list of dictionaries
def update(dict_list, headers):
    ''' arguments: the list of dictionaries and the column label that'll be used to lookup 
        returns: string of lookup values'''

    # get user input
    user_input = input(f"Please input the {headers[0]} you'd like to update data for: ")

    # flag to catch if name is not found
    name_found_flag = False

    # iterate through dictionary list to find data
    for entry in dict_list:
        # if name matches input
        if entry[headers[0]] == user_input:
            # update name found flag to true
            name_found_flag = True
            # data found, now update
            for header in headers:                  # using headers here to account for variable width CSVs
                entry[header] = input(f"Please input new {header}: ")

    # if name wasn't found, return None
    if name_found_flag:
        return dict_list
    else: 
        return None

# function to delete data from list of dictionaries
def delete(dict_list, headers):
    ''' arguments: the list of dictionaries and the column label that'll be used to lookup 
        returns: string of lookup values'''

    # get user input
    user_input = input(f"Please input the {headers[0]} you'd like to delete data for: ")

    # flag to catch if name is not found
    name_found_flag = False

    # iterate through dictionary list to find data
    for i in range(len(dict_list)-1,-1,-1):
        # if name matches input
        if dict_list[i][headers[0]] == user_input:
            # update name found flag to true
            name_found_flag = True
            # data found, now delete
            dict_list.pop(i)

    # if name wasn't found, return None
    if name_found_flag:
        return dict_list
    else: 
        return None

# function for transforming the dictionary list to a csv-ready string
def dict_list_to_csv_string(dict_list, headers):
    ''' arguments: list of dictionaries and a list of header words
        return: a csv string ready for writing to csv '''

    # declare return string as empty
    return_string = ''

    # print out headers first
    for header in headers:
        return_string += header + ','
    # after itering through all columns, slice off last character (the ',')  and add a newline
    return_string = return_string[:-1:1] + '\n'

    # iterate through dict_list
    for row in dict_list:
        # iterate through each header
        for col in row:
            # update return string
            return_string += row[col] + ','
        
        # after itering through all columns, slice off last character (the ',')  and add a newline
        return_string = return_string[:-1:1] + '\n'

    # return string
    return return_string


# main

# open file
filename = 'lab23_spreadsheet.csv'
lines = open_file(filename)


# get dictionary from csv
dict_list = get_dictionary(lines)
# get header by seperating out commas on first line
header = lines[0].split(',')
# print final dict
print(dict_list)


## version 2: CRUD REPL
while True:
    # get operation input
    user_operation = input("\nCommands:\n(c) create\n(r) retrieve\n(u) update\n(d) delete\n(s) show data\n(w) write to file\n(q) quit\nPlease make selection: ")
    user_operation = user_operation.lower()

    # --------------------------------   initiate action depending on input   -----------------------------
    # create
    if user_operation == 'c':
        dict_list.append(create(header))

    # retrieve
    elif user_operation == 'r':
        # get lookup data
        lookup_data = retrieve(dict_list, header[0])       # hardcoding the lookup string since we only want to look up by name
        # if lookup was not found in data
        if not lookup_data:
            print(f"That {header[0]} was not found.")
        else:
            print(lookup_data)

    # update
    elif user_operation == 'u':
        # get updated list of dictionaries
        updated_dict = update(dict_list, header)
        # if dictionary was successully updated, updated dict_list
        if updated_dict:
            dict_list = updated_dict.copy()
        else:
            print("Data not successfully updated")

    # delete
    elif user_operation == 'd':
        # get updated list of dictionaries
        updated_dict = delete(dict_list, header)
        # if dictionary was successully updated, updated dict_list
        if updated_dict:
            dict_list = updated_dict.copy()
        else:
            print("Data not found, delete was unsuccessful")

    # show data
    elif user_operation == 's':
        print(dict_list) 

    # write to file
    elif user_operation == 'w':
        # get output string
        output_string = dict_list_to_csv_string(dict_list, header)

        # write output string
        print(f'test of output_string {output_string}')
        if write(filename, output_string):
            print("Write completed successfully")  
        else:
            print("Write unsuccessful")

    # quit
    elif user_operation == 'q':
        print("Quitting program.")
        break
    # unknown input
    else:
        print(f'user input is {user_operation}')
        print("Bad input, please try again.\n")
