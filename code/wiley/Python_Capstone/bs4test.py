#messing with the beautifulsoup4 module
'''You can apply these two methods to either initial the soup object or Tag object
find() searchs for the first matching tag, and returns a Tag Object
find_all() searches for all matching tags, and returns a resultset object

you can extract information from from a tag object using these two attributes:
text extracts the text of a Tag object, and returns a string/
contents extracts the children of a tag and returns a list of Tas and strings.'''
import requests
from bs4 import BeautifulSoup
import os #use later to call a command line command to downlows the video with youtube_dl
import string
r = requests.get('https://www.basketball-reference.com/teams/DAL/2020.html')
soup = BeautifulSoup(r.text, 'html.parser')
results = soup.find_all('span', attrs={'class':'count win'})
#print(results)
record = []
for result in results:
    record.append(result.contents)


recent_win = record[-1]
string_win = str(recent_win)
#''.join(recent_win)

string_win = string_win[5:-2]
for char in string_win:
    if char not in string.ascii_letters:
        string_win = string_win.replace('@', '')
string_win += " full game highlights"
print(string_win)

