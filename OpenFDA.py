from bs4 import BeautifulSoup
from selenium import webdriver
import time

<<<<<<< Updated upstream
drug_name = input("Enter the name of the drug: ")

html = "https://www.goodrx.com/" + drug_name


driver = webdriver.Chrome()
driver.get(html)
time.sleep(3)

soup = BeautifulSoup(driver.page_source,'lxml')

for a in soup.find_all('a',href=True):

    print ("Found the URL:",a['href'])

=======
# Get the drug name from the user
drug_name = input("Enter the name of the drug: ")

# Set the API endpoint
api_endpoint = "https://data.medicaid.gov/resource/nqzp-d4kc.json"

# Set the API parameters
params = {'name': drug_name}

# Make the API call
response = requests.get(api_endpoint, params=params)

# Check if the API returned a successful response
if response.status_code == 200:
    # Parse the JSON data
    data = json.loads(response.text)
    # Extract the NADAC price from the JSON data
    NADAC_price = data[0]['nadac_per_unit']
    # Print the NADAC price
    print("The NADAC price for " + drug_name + " is $" + NADAC_price)
else:
    print("Error: Could not retrieve data from the API.")
>>>>>>> Stashed changes
