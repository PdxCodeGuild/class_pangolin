'''This is a simple script that uses beautiful soup to webscrape the most recent
win for a selected NBA and downloads the highlights via the youtube_dl module. 
Search results are often dependent upon the youtube search algorithm.  '''

import requests
from bs4 import BeautifulSoup
import os 
import datetime
import string
from pprint import pprint
from team_links import team_links, easy_links
import re

print(f'''\n\n\t\t---Welcome to highlights.py---
A simple program to download the latest highlights of your favorite NBA team.
Here is a list of abbreviated team names for you to choose from and select.\n''')
pprint(easy_links)

select_team = input("\nWhat is the abbreviated name of the team you would like to select?>>").lower()

if select_team in team_links.keys():
    team_link_var = team_links.get(select_team)
else:
    print("A value error occured.  Please select a valid team. Terminating script.")
    exit()


#Make request object and get the source code for scaping
r = requests.get(team_link_var)
soup = BeautifulSoup(r.text, 'html.parser')
#find all instances of "count win" and form a list of all wins
results = soup.find_all('span', attrs={'class':'count win'})
#append the contents of all results to a list.  The last item of the list is the most recent win.
record = []
for result in results:
    record.append(result.contents)
string_win = str(record[-1])
print(f"Last win for {select_team}:\n{string_win}")
yt_regex = re.findall("[A-Z]{3}", string_win)
yt_regex = yt_regex[0:2]
yt_regex = ' '.join(yt_regex)
yt_regex = re.sub("POR", "PDX", yt_regex)


#strip the most recent  win of unneccesary characters and add "full game highlights".
string_win = string_win[5:-2]
string_win = string_win.replace(',', '').replace('@', '')
string_win_jumble = string_win.replace(' ','')

def win_date_format(string_win_jumble):
    '''win_date_format is a function that takes in one parameter: a string that starts with a date.
    It then returns the date that the string started with, ending at the numerical day value.'''
    new = list(string_win_jumble[0:5])
    if new[-1] not in string.digits:
        new[-1] = ''
    string_win_date = ''.join(new) +"2019"
    return string_win_date


#get todays date, and get length of time between today and last win date
today = datetime.datetime.today()
todaystr = today.strftime("%b %d")
last_win_date = datetime.datetime.strptime((win_date_format(string_win_jumble)), '%b%d%Y')
since_win = today - last_win_date


def happy_save():
    '''happy_save compares todays date to the last recorded win.
    If it has been less than 7 days since the win, it will download the youtube video of the game.
    If not, it will do something else. '''
    if since_win < datetime.timedelta(days = 7):
        print("What a win! Enjoy the highlights!")
        os.system(f'py -m youtube_dl "ytsearch:\'{yt_regex +  " full game highlights"}\'"')
        
    
    if since_win > datetime.timedelta(days = 7):
        print(f"No recent wins this week. The most recent win was {last_win_date}. It has been {since_win} since the last win for {select_team}.")





happy_save()
