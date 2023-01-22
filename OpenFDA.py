from bs4 import BeautifulSoup
from selenium import webdriver
import time

drug_name = input("Enter the name of the drug: ")

html = "https://www.goodrx.com/" + drug_name


driver = webdriver.Chrome()
driver.get(html)
time.sleep(3)

soup = BeautifulSoup(driver.page_source,'lxml')

for a in soup.find_all('a',href=True):

    print ("Found the URL:",a['href'])

driver.close()