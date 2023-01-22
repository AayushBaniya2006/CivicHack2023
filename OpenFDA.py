import requests
import json

drug_name = input("Name of the medicine:")
api_endpoint = "https://api.fda.gov/drug/event.json?search=patient.drug.openfda.brand_name:"
response = requests.get(api_endpoint + drug_name + "&limit=1")

# Check if the API returned a successful response
if response.status_code == 200:
    # Parse the JSON data
    data = json.loads(response.text)
    # Extract the price from the JSON data
    price = data['results'][0]['patient']['drug'][0]['openfda']['price_and_pack_size']
    # Print the price
    print("Price of " + drug_name + ": " + price)
else:
    print("Error: Could not retrieve data from the API.")