#Bieschke Quote Generator.py 
#intent: take quotes from favqs.com and manipulate them
import random
import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass

#remove type=author to search for all quotes regarding Confucius
#change filter=Confucius to search for a different author
#quotes_url = 'https://favqs.com/api/quotes/?filter=Confucius&type=author'
#headers = {'Authorization': 'Token token="4b3888849b4ef0bec9f217ffd39869a9"'}

#timeout=(2, 5)
#the first element being a connect timeout 
#(the time it allows for the client to establish a connection to the server), 
#and the second being a read timeout (the time it will wait on a response 
#once your client has established a connection)

def rand_quotes():
    print("Hello! We're working with famous quotes today. You can also press q or 1 to quit.")
    quote_gen = input("Would you like to work with random quotes?")
    if quote_gen in ("y", "yes"):
        quotes_url = f'https://favqs.com/api/quotes/'
        headers = {'Authorization': 'Token token="4b3888849b4ef0bec9f217ffd39869a9"'}
        return quotes_url, headers
    elif quote_gen in ('q', '1'):
        print("Sayonara!")
        quit()        
    else:
        return prompt()

def prompt():   #Author's names must be typed in exactly
    query = input("Would you like to search by author, word, or tag?")
    if query in ("a", "author"):
        author = input("Who would you like to search for?").capitalize()
        quotes_url = f'https://favqs.com/api/quotes/?filter={author}&type=author'
        headers = {'Authorization': 'Token token="4b3888849b4ef0bec9f217ffd39869a9"'}
        return quotes_url, headers

    elif query in ("w", "word"):
        word = input("What word would you like to search for?")
        quotes_url = f'https://favqs.com/api/quotes/?filter={word}'
        headers = {'Authorization': 'Token token="4b3888849b4ef0bec9f217ffd39869a9"'}
        return quotes_url, headers

    elif query in ("t", "tag"):
        tag = input("What tag would you like to search for?")
        quotes_url = f'https://favqs.com/api/quotes/?filter={tag}&type=tag'
        headers = {'Authorization': 'Token token="4b3888849b4ef0bec9f217ffd39869a9"'}
        return quotes_url, headers

    elif query in ('q', '1'):
        print("Sayonara!")
        quit()

    else:
        print("sorry, just authors or words please.")
        return prompt() #recursive reentry

def processing():
    print("\nFabulous quotes! Do you want to mash them up, or create your own?")
    process = input("You can also press q or 1 to quit, or enter to start over\n> ")

    if process in ('m', 'mash'):
        mash(quote1, quote2)

    elif process in ('c', 'create'):
        print("Now you can create your own quotes! We'll be saving them to a .csv")
        file = open("quotes_out.csv", "a")
        user_quote = input("What quote will you grace us with today?")
        file.write(f"{user_quote}\n")
        quote3 = user_quote
        user_quote = input("Lovely! What about a second quote?")
        file.write(f"{user_quote}\n")
        quote4 = user_quote
        print("Let's mash your quotes together!")
        quoteX = mash(quote3, quote4)
        #save(quoteX)
        with open ("quotes_out.csv", "r") as file:
            contents = file.read()
        print(f"Here are the quotes you have saved so far!\n{contents}")
        file.close()

    elif process in ('q', '1'):
        print("Sayonara!")
        quit()

def mash(quote1, quote2):
    punct_list = [':', ',', ' - ', '.']
    for punct in punct_list:
        #print(punct)
        if punct in quote1:
            #print('FOUND PUNCTIONAT')
            quote1 = quote1.split(punct) 
            quote1 = quote1[0]
            quote1 = str(quote1)+(f", {quote2}")
            print(quote1)
            quoteX = quote1
            save(quoteX)
            return
        
    quote2 = quote2.split(punct) 
    quote2 = quote2[0]
    quote2 = str(quote2)+(f", {quote1}")
    print(quote2)
    quoteX = quote2
    save(quoteX)

def save(quoteX):
    save_quote = input("\nGood stuff! Would you like to save that monster mash?")
    if save_quote in ('y', 'yes'):
        with open("quotes_out.csv", "a") as file:    
        #file = open("quotes_out.csv", "a")
            file.write(f"{quoteX}\n")
        print("Saved!\n")

lions = True        
while lions == True:
    quotes_url, headers = rand_quotes()
    #quotes_url, headers = prompt()
    #requests.get(quotes_url, headers=headers)
    response = requests.get(quotes_url, headers=headers, timeout=(2, 5))

    if response:
        print("I'm running! I'M RUNNING!")
    else:
        print('Not Found.')

    results = response.json()
    #print(results)

    #def get_quote(quote1, quote2):
    quote1 = results['quotes'][random.randint(0, 25)]['body']
    quote2 = results['quotes'][random.randint(0, 25)]['body']
    print(quote1)
    print(quote2)
    processing()
    #mash(quote1, quote2)