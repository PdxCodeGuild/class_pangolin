#Bieschke Quote Generator.py 

import requests

r = requests.get('https://favqs.com/api/quotes/?filter=Confucius&type=author', headers={'Authorization': 'Token token="4b3888849b4ef0bec9f217ffd39869a9"'})
print(r.json())