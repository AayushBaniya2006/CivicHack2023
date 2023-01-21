import re
import json
from urllib2 import urlopen

url = 'http://ipinfo.io/json'
response = urlopen(url)
data = json.load(response)

IP=data['ip']
org=data['org']
city = data['city']
country=data['country']
region=data['region']

print('Your IP detail\n ')
print('IP : {4} \nRegion : {1} \nCountry : {2} \nCity : {3} \nOrg : {0}'.format(org,region,country,city,IP))

import pip._vendor.requests 
import requests
from bs4 import BeautifulSoup

r = requests.get('https://do512.com/p/locally-owned-in-austin%27')



soup = BeautifulSoup(r.content, "html.parser")

for link in soup.find_all('p'):
    print(link)