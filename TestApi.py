import requests

response = requests.get("https://api.fda.gov/drug/event.json?limit=1",params="advil")
print(response.text)