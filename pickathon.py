import requests
from bs4 import BeautifulSoup as soup
import smtplib
import pickle
import os
import urllib2

url = 'https://pickathon.com/volunteer/'
file_path = 'pickathon.pkl'
snapshot = ''
response = soup(urllib2.urlopen(url), 'lxml')
content = response.find(name='div', attrs={'class': 'content'})

 # set the old snapshot of webpage to compare
if (os.path.isfile(file_path)):
    download = open(file_path, 'rb')
    unserialized_content = pickle.load(download)
    download.close()
    snapshot = unserialized_content
# if it doesn't exist, store the snaphot
else:
    download = open(file_path, 'wb')
    pickle.dump(content, download)
    download.close()

# send email if the snapshot is not empty and content has changed
if (content != snapshot && snapshot != ''):
    msg = 'Subject: PICKATHON VOLUNTEER OPPORTUNITIES ARE UP'
    fromaddr = 'YOUR_EMAIL'
    toaddrs  = ['EMAIL_ADDRESS_1, EMAIL_ADDRESS_2']

    # setup the email server,
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('YOUR_EMAIL', 'YOUR_PASSWORD')

    # send the email
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()
