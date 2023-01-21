import pip._vendor.requests 
import requests
from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver



def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name")
    }
    return location_data


r = requests.get('https://www.google.com/maps')
 
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
location = get_location()
search = location["city"]

content = soup.find(id = 'searchbox')

driver = webdriver.Firefox()
driver.implicitly_wait(10) # this lets webdriver wait 10 seconds for the website to load
driver.get("https://www.google.com/maps")


text_box = driver.find_element("id", "searchbox")

text_box.send_keys(content) # enter text in input

driver.find_element("id", 'searchbox-searchbutton').click() # click the submit button

driver.quit()     




