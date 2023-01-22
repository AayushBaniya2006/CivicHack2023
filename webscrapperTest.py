import requests

url = "https://api.fda.gov/drug/drugsfda.json?limit=5"
response = requests.get(url)
data = response.json()

for drug in data["results"]:
    for product in drug["products"]:
        print(product["brand_name"])