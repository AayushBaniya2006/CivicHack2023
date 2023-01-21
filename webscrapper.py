import pip._vendor.requests 
import requests
from bs4 import BeautifulSoup

r = requests.get('https://do512.com/p/locally-owned-in-austin%27')



soup = BeautifulSoup(r.content, "html.parser")
print(soup.prettify())
print("x")