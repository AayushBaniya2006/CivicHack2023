from flask import Flask, render_template, request
import requests
from flask import Flask, request, render_template
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('TestMain.html'))


<<<<<<< Updated upstream
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

=======

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        drugNeeded = request.form['drug']
        url = f"https://api.fda.gov/drug/drugsfda.json?limit=68&search={drugNeeded}"
        response = requests.get(url)
        data = response.json()

        for drug in data["results"]:
            for product in drug["products"]:
                if drugNeeded.upper() == product["brand_name"]:
                    method_of_consumption = product["dosage_form"]
                    ingredients = []
                    for ingredient in product["active_ingredients"]:
                        ingredients.append(f"{ingredient['strength']} {ingredient['name']}")
                    return render_template('result.html', method_of_consumption=method_of_consumption, ingredients=ingredients)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> Stashed changes
