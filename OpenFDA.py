import requests
import json

# Get the drug name and location from the user
drug_name = input("Enter the name of the drug: ")
location = input("Enter your location (zip code or city, state): ")

# Set the API endpoint
api_endpoint = "https://www.goodrx.com/api/compare-prices/"

# Set the API parameters
params = {'name': drug_name, 'location': location}

# Make the API call
response = requests.get(api_endpoint, params=params)

# Check if the API returned a successful response
if response.status_code == 200:
    # Parse the JSON data
    data = json.loads(response.text)
    # Extract the cheapest price from the JSON data
    prices = data['prices']
    cheapest_price = min(prices, key=lambda x: x['price'])
    # Print the cheapest price
    print("The cheapest price for " + drug_name + " in " + location + " is $" + str(cheapest_price['price']))
else:
    print("Error: Could not retrieve data from the API. ")
