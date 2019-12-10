'''
Casey Burge
Filename: modest_song_interpeter.py
11/14/2019
'''
from pprint import pprint as pp
import re
import requests
from bs4 import BeautifulSoup
import mingus.core.progressions as progressions
import mingus.core.chords as chords

# welcome message
print("\nHello!\nWelcome to Modest Song Interpreter.")
# define user_url 
user_url = input("Please enter the URL of the song you'd like to learn: ").lower()

# use requests module to scrape HTML
r = requests.get(user_url)

# parse HTML using BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')

def title(soup):
    # use find_all to find title (tag: <title>)
    title = soup.find_all('title')
    title = str(title)
    title = title.replace("[<title>", "")
    title = title.replace("</title>]", "")
    return title 
title(soup)

def key(soup):
    # find song key by applying (regular expressions) re.compile & re.findall to soup 
    key_filter = re.compile('strKey = "(.*)";')
    key_list = re.findall(key_filter, str(soup))
    key = key_list[0]
    return key
key(soup)

def lines_results(soup):
    # use find_all to find lines_results (tag: <pre>)
    lines_results = soup.find_all('pre')
    # iterate over lines_results, convert to text & append to lines_list
    lines_list = []
    for i in lines_results:
        lines_list.append(i.text)
    # create lines_str by joining lines_list
    lines_str = lines_list[0]
    return lines_str
lines_results(soup)

def isolate_chords(soup):
    # isolate chords by splitting lines_str, appending every other line to c_list (removes lyrics)
    sections = lines_results(soup).split("\r\n\r\n")
    sections = [section.split("\n") for section in sections]
    c_list = []
    for i in sections:
        c_list.append(i[::2])
    return c_list
isolate_chords(soup)

def clean_chords(soup):
    # replace uneeded characters to isolate shorthand chord names
    clean_c_list = [[line.replace("\r", "") for line in section] for section in isolate_chords(soup)]
    clean_c_list = [[line.replace(" ", "") for line in section] for section in clean_c_list]
    clean_c_list = [[line.replace("\t", "") for line in section] for section in clean_c_list]
    clean_c_list = [[line.replace("Intro", "") for line in section] for section in clean_c_list]
    clean_c_list = [[line.replace("Instrumental", "") for line in section] for section in clean_c_list]
    clean_c_list = [[line.replace("x", "") for line in section] for section in clean_c_list]
    clean_c_list = [[line.replace("\r", "") for line in section] for section in clean_c_list]
    clean_c_list = [[line.replace("(", "") for line in section] for section in clean_c_list]
    clean_c_list = [[line.replace(")", "") for line in section] for section in clean_c_list]
    clean_c_list = [[line.replace("solo", "") for line in section] for section in clean_c_list]
    clean_c_list = [[line.replace("2", "") for line in section] for section in clean_c_list]
    clean_c_list = [[line.replace("4", "") for line in section] for section in clean_c_list]
    clean_c_list = [[line.replace("8", "") for line in section] for section in clean_c_list]
    clean_c_list = [[line.replace("/", "") for line in section] for section in clean_c_list]
    clean_c_list = [[line.replace(":", "") for line in section] for section in clean_c_list]
    # split clean_c_list by uppercase characters to separate shorthand chord names
    clean_c_list = [[re.findall('[A-Z][^A-Z]*', line) for line in section] for section in clean_c_list]
    return clean_c_list

def clean_duplicates(soup):
    # remove duplicate lists from clean_c_list
    no_dups = []
    for elem in clean_chords(soup):
        if elem not in no_dups:
            no_dups.append(elem)
    dup_free_c_list = no_dups
    return dup_free_c_list

# attempt at formatting chords according to sections of the song
# song_sections = [' '.join([str(line) for line in section]) for section in clean_duplicates(soup)]

def longhand_trans(soup):
    # iterate over line in section in dup_free_c_list, convert to longhand & append to longhand_chords list
    longhand_chords = []
    for section in clean_duplicates(soup):
        for line in section:
            for chord in line:
                longhand_chords.append(chords.from_shorthand(chord))
    return longhand_chords
longhand_trans(soup)

def gen_numerals(soup):
    # create prog_numerals list by passing longhand_chords, key & True (asks for numerals) to progressions.determine
    prog_numerals = progressions.determine(longhand_trans(soup), key(soup), True)
    return prog_numerals

# define user_op
user_op = input("\nThank you.\nWhat would you like to see?:\n-Lyrics & chords (l)\n-Shorthand chord names (s)\n-Chords in numerals (n)\n").lower()
# define op_list
op_list = ['l', 's', 'n']

while True:
    if user_op not in op_list:
        user_op = input("Please select from the following options:\nLyrics & chords (l)\nShorthand chord names (s)\nChords in numerals (n)\n").lower()
    else:
        break

if user_op == 'l':
    print(f"\n{title(soup)}\n\nKey: {key(soup)}\n\n{lines_results(soup)}")

if user_op == 's':
    print(f"\n{title(soup)}\n\nKey: {key(soup)}\n\nBelow are the shorthand chord names by song section in order:\n-Intro\n-Verse\n-Chorus\n-Instrumental Bridge\n-Chorus/Outro\n")
    pp(clean_duplicates(soup))

if user_op == 'n':
    print(f"\n{title(soup)}\n\nBelow are the chords in numerals.\n\n{gen_numerals(soup)}\n")