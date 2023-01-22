import pip._vendor.requests 
import requests
from bs4 import BeautifulSoup
# A bunch of flask tutorial shit
from flask import Flask

app = Flask(__name__)

#Routing -> Ties a url from a HTML website to  Python function. I think .route is the routing

#@ signifies a decorator - a decorator is a way to wrap a function and modify its behavior
@app.route('/') #Connects the main page of the HTML to this function? Not sure on this part :/
def index(): #Defines the main page
    return 'This is the homepage' # This is what is returned when we head to the main(home page)

@app.route('/tuna')#Edit this later -> This basically sets a route to a another page from main. change the words behind the / to change the page you want to go to
def tuna():
    return '<h1>This is a test<h1>'#Return values can run HTML

if __name__== "__main__": #This check make sure that the webserver when this file is called directly
    app.run(debug=True) #This starts the app
    

#End of flask stuff.
r = requests.get('https://do512.com/p/locally-owned-in-austin%27')

print(r)

soup = BeautifulSoup(r.content, "html.parser")
print(soup.prettify())