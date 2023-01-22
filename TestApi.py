import requests
from bs4 import BeautifulSoup

# Get the drug name from the user
drug_name = input("Enter the name of the drug: ")

# Set the GoodRx URL
url = "https://www.goodrx.com/" + drug_name

# Make the GET request to the website
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find the price element
price_element = soup.find("span", {"class": "drug-price_price"})

# Extract the price from the element
price = price_element.text

# Print the price
print("The price for " + drug_name + " on GoodRx is: " + price)