# Shawn Stolsig
# PDX Code Guild 
# Assignment: Lab 24 - Rain Data
# Date: 11/1/2019

import matplotlib.pyplot as plt
import datetime

# function for opening file and getting input list of string lines
def open_file(filename):
    ''' arguments: filename
        returns: header list and data as a tuple '''

    with open(filename,'r') as f:
        lines = f.read().strip()
        lines = lines.split('\n')

    # return just the data starting at line 11)                  
    return lines[11::]

# function for translating list of strings into useable data
def format_data(string_list):
    ''' argument: list of strings, each string being a line of the input file,
        return: a dictionary of dictionaries, one dict per day '''

    # Data structure: 
    # Each day will have it's own dictionary in this format:
    # { <dateobject>: { 'total': int of daily total, 
    #                   'hr_values: [rain at hr 0, rain at hr 1, ..., rain at hour 23] } 
    #                 }

    # declare return list
    parent_dict = {}

    # iterate through each line in the input list of string
    for day in string_list:
        # strip whitespace for day...should only apply to first day
        stripped_day = day.strip()

        # split on white space
        split_day = stripped_day.split()

        # create new dictionary for that day
        this_day_datetime_object = datetime.datetime.strptime(split_day.pop(0), '%d-%b-%Y')     # pop off index 0, this is the day
        this_day_total = int(split_day.pop(0))                                                  # pop off index 0 again, this is now the daily total

        # create new key/value pair in parent dictionary.  hourly totals are added as a list of characters
        parent_dict[this_day_datetime_object] = {'total': this_day_total, 'hr_values':split_day}

    # return parent_dict
    return parent_dict

# function for returning a certain day's info
def get_day_total(data, month, day, year):
    ''' arguments: data list of dictionaries, month/day/year in '04' 'FEB' '2019' format
        returns: int of total rainfall '''

    # turn input into datetime obj
    date_object = datetime.datetime.strptime(f'{day}-{month}-{year}', '%d-%b-%Y')

    # return int 
    return  data[date_object]['total']

# function to return mean of all day values
def get_mean(data):
    ''' arguments: data dictionary
        returns: mean of all daily values '''

    # get total number of elements
    total_days = len(data.keys())

    # variable for tracking sum
    sum = 0

    # iterate through each day
    for day in data:
        # add total to sum
        sum += data[day]['total']

    # return mean
    return sum/total_days

# function to get variance of all day values
def get_variance(data, mean):
    ''' arguements: dataset dictionary and mean value as float
        returns: variance of daily totals '''

    # define return variable
    running_sum = 0
    total_num_days = 0

    # for each day in data set
    for day in data:
        #add (n - mean)**2 
        running_sum += (data[day]['total'] - mean) ** 2
        total_num_days += 1

    # 1/n * running_sum is variance, so return that value
    return running_sum/total_num_days

# function for getting highest rain day
def get_highest_total(data):
    ''' arguments: dataset dictionary
        returns: highest day as a dateobject '''

    # variable for tracking max
    max = 0

    # iterate through every day
    for day in data:
        # if day totla is greater than max
        if data[day]['total'] > max:
            # set equal to max
            max = data[day]['total']
            # get dateobject for return
            return_date_object = day

    # return dateobject
    return return_date_object

# function for getting year average
def get_year_average(data, year):
    ''' arguments: dataset dictionary, year
        return: average rain for that year as a float '''

    # sum and num variables needed for mean cal
    sum = 0
    num_days = 0

    # make sure an int is passed in 
    year = int(year)

    # iterate through dataset
    for day in data:
        # if day.year matches desired year
        if day.year == year:
            # add day total rain to sum
            sum += data[day]['total']
            # increment num_days
            num_days += 1

    # return mean
    try:
        return sum/num_days                 
    except ZeroDivisionError:
        print("No days in that year found")
        return 0

# function for getting highest year average
def get_highest_year(data):
    ''' arguments: dataset dictionary,
        return: tuple with int of the year with highest rain average and the value for that year '''

    # variable for tracking max year
    max_year = 0
    max_year_value = 0

    # for each year
    for i in range(1998,2020):
        year_average = get_year_average(data,i)
        if year_average > max_year_value:
            max_year = i
            max_year_value = year_average

    # return max year
    return max_year, round(max_year_value,2)

# main

# open file
filename = 'harney_pump.rain'
rain_data_string_list = open_file(filename)

# translate data into a useable list of dictionaries
data = format_data(rain_data_string_list)

# get mean of daily totals
mean = round(get_mean(data),2)                              # rounded to two decimal places
print(f'The mean from this input data is: {mean} inches.')

# get the variance
variance = round(get_variance(data, mean),2)                # rounded to two decimal places
print(f'The variance for this input data is: {variance} inches.')

# get highest total day 
highest_day = get_highest_total(data)
print(f"The highest day is {highest_day.month}/{highest_day.day}/{highest_day.year} with {data[highest_day]['total']} inches. ")

# get year with highest average
most_year, most_year_avg = get_highest_year(data)
print(f"Year with the most rain was: {most_year} with {most_year_avg} inches of rain on average.")

# for matplot

# date vs daily total
# initialize lists for x and y values
x_values = []
y_values = []
# use a counter of tracking days
counter = 0
# iterate through each day in the dataset
for day in data:
    # add day to the x_value list
    x_values.append(counter)                # just using a counter for each day to make it easy to display
    # add daily total as a y value 
    y_values.append(data[day]['total'])
    counter += 1
# show rainfall vs day plot
plt.plot(x_values, y_values)
plt.show()

# monthly totals, average across multiple years
# create dictionary to store monthly totals
monthly_totals = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}
# iterate through dataset
for day in data:
    # add that day's total to the appropriate month
    monthly_totals[day.month] += data[day]['total']
# figure out how many years to average by
num_years = len(range(1998,2020))
# divide each month by number of years...using a dict comprehension
monthly_totals_avg = { key: (value/num_years) for key,value in monthly_totals.items() }
# convert dictionary into two lists of x/y values for plotting
x2_values = list(monthly_totals_avg.keys())
y2_values = list(monthly_totals_avg.values())
# show rainfall avg by month fault plot
plt.plot(x2_values, y2_values)
plt.show()

# total yearly rainfall by year
# create dictionary and populate it with each year as a key and zero as its total rainfall
yearly_totals = {}
for year in range(1998,2020):
    yearly_totals[year] = 0
# iterate through each day in dataset
for day in data:
    # add that day's total to the appropriate year total
    yearly_totals[day.year] += data[day]['total']
# extract x and y value lists from dictionary
x3_values = list(yearly_totals.keys())
y3_values = list(yearly_totals.values())
# show rainfall totals by year plot
plt.plot(x3_values, y3_values)
plt.show()