# python_final.py
# weather update
# Python final project
# Jeff Smith

import string
import requests
from pprint import pprint
import smtplib 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# OpenWeatherMap API key


# Search criteria pulling current (<10min) for Portland, OR. Return 'Imperial' results. 
# Future version will be searchable for any city.



res = requests.get(url) # Retrieve the page
data = res.json() # Put the local data into a searchable format.

# pprint(data) # Allows you to visually identify the location of your target data.

# Specify selected data points
description = data['list'][0]['weather'][0]['description']
wind_speed = data['list'][0]['wind']['speed']
temp = data['list'][0]['main']['temp']
humid = data['list'][0]['main']['humidity']

 # create 'body' of outgoing message
c = 'Current Conditions : {}'.format(description)
t = 'Temperature : {} degrees'.format(temp)
w = 'Wind : {} mph'.format(wind_speed)
h = 'Humidity: {} %'.format(humid)
# c = '\033[4mCurrent Conditions\033[0m: {}\n'.format(description)\n'
# t = 'Temperature : {}\u00B0\n'.format(temp)
# w = 'Wind : {} mph\n'.format(wind_speed)
# h = 'Humidity: {} %\n'.format(humid)
    


smtp = "smtp.gmail.com"
port = 587
server = smtplib.SMTP(smtp,port) 
server.starttls() # Starting the server
sl = server.login(email,pas) # Pass login info
# print(server.login(email,pas)) # In the event of mail login issues
msg = MIMEMultipart()
msg['From'] = email
msg['To'] = to
msg['Subject'] = f"Weather Report{c + t + w + h}" 
# msg['Subject'] = "Weather Report\n\n" 
body = f"Weather Report\n\n{c, t, w, h}\n"
msg.attach(MIMEText(body, 'plain'))
server.sendmail(msg['From'], msg['To'], msg.as_string())

# Quit the SMTP server
server.quit()

# Future additions to include: 
# 1) SMS to replace email 2)Search for any city 3)choice of target data 
# 4)daily update/hourly check for triggers 5)trigger alert