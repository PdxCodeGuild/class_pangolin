import requests
from bs4 import BeautifulSoup
import pandas as pd

#%matplotlib inline

url = "https://www.outsideonline.com/2393422/best-sport-climbing-areas-crags-us" #grabing a url that is not a bad html link

r = requests.get(url) 
#print(r.text[0:500])
soup = BeautifulSoup(r.text, 'html.parser') #takes your request and puts it in text format
results = soup.findAll('strong') #searching for all strong tags within the link

actual_results = results[1:11] # 12 results found but 1 not needed

new = ",".join(map(str,actual_results)) #joining the results together
new = new.replace('.',',')
#print(new)
#new2 = actual_results.strong.decompose()
new2= new[8:-9].split('</strong>,<strong>') #cool split method using tags

new3 = [str(val).split(",") for val in new2] 
#writing the DataFrame
df = pd.DataFrame(new3, index=None, columns = ['Rank','Place','Location'])
#new3 = new2.split()
print(df)
df.to_csv('10_climing_destinations.csv')

#a ='\n'.join(new2)

#a = new2[1]
#print(a)
# getting_raw = new2.replace('<strong>','')
# getting_raw = getting_raw.replace('</strong>','')

# print (getting_raw)

# df = pd.DataFrame(getting_raw)
# df.columns = ['rank', 'name', 'place']