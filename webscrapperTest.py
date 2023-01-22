import requests
from flask import Flask, request, render_template
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('TestMain.html'))


url = "https://api.fda.gov/drug/drugsfda.json?limit=68"
response = requests.get(url)
data = response.json()

template = env.get_template('TestMain.html')
data = "This is data from python"
output = template.render(data=data)

drugNeeded = input("Enter drug: ")
for drug in data["results"]:
    for product in drug["products"]:
        if drugNeeded.upper() == product["brand_name"]:
            print("Method of Consumption: " + product["dosage_form"])
            print("Indredients:")
            for ingredient in product["active_ingredients"]:
                print(ingredient["strength"]+" " + ingredient["name"])
            break

