import requests
from bs4 import BeautifulSoup
import pandas as pd

#%matplotlib inline

url = "https://www.outsideonline.com/2393422/best-sport-climbing-areas-crags-us"

r = requests.get(url)
#print(r.text[0:500])
soup = BeautifulSoup(r.text, 'html.parser')
results = soup.findAll('strong')

actual_results = results[1:11]
#actual_results = actual_results.replace('.',',')

new = ",".join(map(str,actual_results))
#new2 = actual_results.strong.decompose()
new2= new[8:-9].split('</strong>,<strong>')
#print(new2)

new3 = [str(val).split(",") for val in new2]
print(new3)

df = pd.DataFrame(new3, index=None, columns = ['place','location'])
#new3 = new2.split()
print(df)
#a ='\n'.join(new2)

#a = new2[1]
#print(a)
# getting_raw = new2.replace('<strong>','')
# getting_raw = getting_raw.replace('</strong>','')

# print (getting_raw)

# df = pd.DataFrame(getting_raw)
# df.columns = ['rank', 'name', 'place']
# df.to_csv('test_text.csv')
