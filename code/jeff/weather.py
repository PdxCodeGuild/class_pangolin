# weather.py
# Python final project
# Jeff Smith
import string
import requests
from pprint import pprint
import smtplib 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# OpenWeatherMap API key

# Search criteria pulling current +- 10min, for Portland, OR. Return 'Imperial' results.
url = 'http://api.openweathermap.org/data/2.5/forecast?id=4720131&APPID=248f86c4f28e22722ba6efee4a3066db&units=imperial'

res = requests.get(url) # Retrieve the page
data = res.json() # Put the local data into a searchable format.
#pprint(data)
# Allows you to visually identify the location of your target data.
# 
description = data['list'][0]['weather'][0]['description']
wind_speed = data['list'][0]['wind']['speed']
temp = data['list'][0]['main']['temp']
humid = data['list'][0]['main']['humidity']

# def body():
    # create 'body' of outgoing message
description = data['list'][0]['weather'][0]['description']
wind_speed = data['list'][0]['wind']['speed']
temp = data['list'][0]['main']['temp']
humid = data['list'][0]['main']['humidity']

c = '\033[4mCurrent Conditions\033[0m:\n'
t = 'Temperature : {}\u00B0\n'.format(temp)
w = 'Wind : {} mph\n'.format(wind_speed)
d = 'Description : {}\n'.format(description)
h = 'Humidity: {} %\n'.format(humid)
    
    # return c + t + w + d + h

# print(body())

smtp = "smtp.gmail.com" #outgoing server for sms
port = 587
server = smtplib.SMTP(smtp,port) # initialize smtp server
server.starttls()# Starting the server
sl = server.login(email,pas)# Pass login info
#print(server.login(email,pas))# Pass login info
msg = MIMEMultipart()# Use the MIME module to structure our message.
msg['From'] = email
msg['To'] = to
msg['Subject'] = f"Weather Report\n\n{c + t + w + d + h}" 
#msg['body'] = body
msg.attach(MIMEText(msg['Subject'], 'plain'))
server.sendmail(msg['From'], msg['To'], msg['Subject'])

# # lastly quit the server
server.quit()
