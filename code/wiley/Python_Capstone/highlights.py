'''This is a simple script that uses beautiful soup to webscrape the most recent
win for the Dallas Mavericks and download the highlights via the youtube_dl module. '''

import requests
from bs4 import BeautifulSoup
import os #use later to call a command line command to downlows the video with youtube_dl
#import string
import datetime

#Make request object and get the source code for scaping
r = requests.get('https://www.basketball-reference.com/teams/DAL/2020.html')
soup = BeautifulSoup(r.text, 'html.parser')
#find all instances of "count win" and form a list of all wins
results = soup.find_all('span', attrs={'class':'count win'})
#append the contents of all results to a list.  The last item of the list is the most recent win. 
record = []
for result in results:
    record.append(result.contents)
string_win = str(record[-1])

#strip the most recent  win of unneccesary characters and add "full game highlights".
string_win = string_win[5:-2]
string_win = string_win.replace('@', '') + " full game highlights"
print(string_win)



today = datetime.datetime.today()
todaystr = today.strftime("%b %d")
print(today)
print(f"Todays date is {todaystr}.")

def get_game_date(string_win):
    win_date = string_win[0:6]
    return win_date

string_date = string_win[0:5] + " 2019"
last_win_date = datetime.datetime.strptime(string_date, '%b %d %Y')
print(last_win_date)
since_win = today - last_win_date
print(since_win)





#use os.system module and the youtube_dl call to download the video
#os.system(f'py -m youtube_dl "ytsearch:\'{string_win}\'"')