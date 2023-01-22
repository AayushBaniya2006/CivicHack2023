import time
from email import header
import pip._vendor.requests 
import requests
from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# url = "https://www.goodrx.com/"
# html = requests.get(url)
# header = {'origin': 'https://www.goodrx.com/'} 
# r = BeautifulSoup(html.content , 'lxml')

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.implicitly_wait(0.5)
#launch URL
driver.get("https://www.google.com/")
#identify search box
m = driver.find_element_by_name("q")
#enter search text
m.send_keys("Tutorialspoint")
time.sleep(0.2)
#perform Google search with Keys.ENTER
m.send_keys(Keys.ENTER)




