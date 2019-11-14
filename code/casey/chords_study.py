'''
Objectives:

    - Scrape HTML from tab/sheet music sites: 2 functions
        - Find and organize chord names
    - Print original progression for user
    - Use chords.short_hand & progression.determine to determine            numerals: 2 functions
    
    - *Possible*
        
        - Give user an option to change the key of the song in              either direction: at least 1 function
        - Give user an option to replace I & IV with relative minors: at    least 1 function
        - Provide theoretically sound chord alternatives: at least 1        function

    Modules: - pprint 
             - mingus chords 
             - mingues progressions 
             - requests
             - beautifulsoup4
             - re (regular expressions)
             - pprint
'''
from pprint import pprint as pp
import re
import requests
from bs4 import BeautifulSoup
import mingus.core.progressions as progressions
import mingus.core.chords as chords

# use requests module to scrape HTML
r = requests.get('https://www.e-chords.com/chords/the-beatles/let-it-be')

# parse HTML using BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')

# find song key by applying (regular expressions) re.compile & re.findall to soup 
key_filter = re.compile('strKey = "(.*)";')
key_list = re.findall(key_filter, str(soup))
key = key_list[0]
print(key)

# use find_all to find chords (tag: <u>)
results = soup.find_all('u')
# iterate over results, convert to text & append to chords_list
chords_list = []
for i in results:
    chords_list.append(i.text)
# create chords by joining chords_list
chords_str = ", ".join(chords_list)

# iterate over chords_list, convert to longhand & append to longhand_chords list
longhand_chords = []
for i in chords_list:
    longhand_chords.append(chords.from_shorthand(i))
# print(longhand_chords)

# create prog_numerals list by passing longhand_chords, key & True (asks for numerals) to progressions.determine
prog_numerals = progressions.determine(longhand_chords, key, True)

print(prog_numerals)

# pat_count = {}
# for count in range(2, 8):
#     for i in range(0, len(prog_numerals) - count):
#         key = tuple((str(prog_numerals[i + j]) for j in range(count)))
#         if key in pat_count: 
#             pat_count[key] += 1
#         else:
#             pat_count[key] = 1

# pp(pat_count)