# Shawn Stolsig
# PDX Code Guild 
# Assignment: Optional Lab - Crime Data
# Date: 11/6/2019

import math

# function for opening file
def initialize_data(filename):
    ''' parameters: filename to open , return list nested with dict dataset '''

    # open file, store each line in list 'lines'
    with open(filename) as f:
        lines = f.read().strip().split("\n")                # remove whitespace at start/end of file and split on newlines

    # initialize dataset and header list
    dataset = []
    header = lines[0].replace('"', '').split(',')            # splitting each line on ,  and also strip out all "

    # iterate through lines after header
    for i in range(1,len(lines)):
        # create split line
        split_line = lines[i].replace('"','').split(',')
        # create tuple list to hold key/value pairs while iterating through header
        tup_list = []
        # iterate through header
        for j in range(len(header)):
            # append each key/value pair to tuple list as a tuple
            tup_list.append( (header[j].strip(), split_line[j].strip()) )       #striping off some extra whitespace that was between commas

        # append tuple list to dataset as a dict 
        dataset.append(dict(tup_list))

    # reaturn dataset
    return dataset
    
# function for getting dict of crimes and how often they occured
def get_crime_statistics(dataset):
    ''' parameters: dataset (list of dicts)         returns: dict of each crime and how many times they occured '''

    # crime stat dataset
    crime_stats = {}

    # iterate through each crime in dataset
    for crime in dataset:
        # if check to see if crime type has occured before
        if crime['Major Offense Type'] in crime_stats:
            # if it has, increment that value by one
            crime_stats[crime['Major Offense Type']] += 1
        # if crime has not occured
        else:
            # create key/value pair with that crime and an init value of 1
            crime_stats[crime['Major Offense Type']] = 1

    # return crime state dict
    return crime_stats

# function for printing crime stats
def print_crime_stats(crime_stats):
    ''' parameters: crime stats dictionary      return: none '''

    print("Number of crime instances: ")
    # iterater through crimes
    for crime in crime_stats:
        # print out a clean formate for each
        print(f"{crime} occured {crime_stats[crime]} times")

    # no return value
    return 

# function for getting most frequent crime
def get_most_frequent_crime(crime_stats):
    ''' parameters: crime stats dict            return: crime and how often committed as tuple '''

    # declare variables to be used
    max = 0
    max_crime = ''

    # iterate through crimes
    for crime in crime_stats:
        if crime_stats[crime] > max:
            max_crime = crime
            max = crime_stats[crime]
    
    return max_crime,max

# function for getting most frequent crime
def get_least_frequent_crime(crime_stats):
    ''' parameters: crime stats dict            return: crime and how often committed as tuple '''

    # declare variables to be used
    min = math.inf
    min_crime = ''

    # iterate through crimes
    for crime in crime_stats:
        if crime_stats[crime] < min:
            min_crime = crime
            min = crime_stats[crime]
    
    return min_crime,min

# get total crimes
def get_total_crimes(crime_stats):
    '''' parameter: crime stats dictionary          return: int of total number of crimes '''

    sum = 0
    for crime in crime_stats:
        sum += crime_stats[crime]

    return sum


# main
while True:
    user_year = input("\nWhich year (from 2011 to 2014) would you like to review? ")
    if user_year in ['2011','2012','2013','2014']:
        break
    else:
        print("Please input year between 2011 and 2014")

# specify file name to open
filename = 'crime_incident_data_' + user_year + '.csv'
# get dataset from file
dataset = initialize_data(filename)

# Figure type of crime statistics
crime_stats = get_crime_statistics(dataset)
# print_crime_stats(crime_stats)
# Specify which crime occured most often
max_crime, max_crime_count = get_most_frequent_crime(crime_stats)
print(f"The most frequent crime in {user_year} is {max_crime} with {max_crime_count} occurances")

# Which crime occured least often?
min_crime, min_crime_count = get_least_frequent_crime(crime_stats)
print(f"The least frequent crime in {user_year} is {min_crime} with {min_crime_count} occurances")

print("\n Proceeding to calculate yearly stats for all input files...\n")

# Year with most crime?
# iterate through each year
crimes_by_year = []
for i in range(2011,2015):
    # specify file name to open
    filename = 'crime_incident_data_' + str(i) + '.csv'
    # get dataset from file
    dataset = initialize_data(filename)
    # populate year/crime list
    crimes_by_year.append( (i,get_total_crimes(get_crime_statistics(dataset))) )

print(f"Crimes by year: {crimes_by_year}")
max_year = crimes_by_year[0][0]
max = crimes_by_year[0][1]

for crime_year in crimes_by_year:
    if crime_year[1] > max:
        max = crime_year[1]
        max_year = crime_year[0]
print(f"The max crime year was {max_year} with {max} crimes total.\n")
