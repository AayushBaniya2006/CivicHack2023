
# A bunch of flask tutorial shit
from flask import Flask, request, render_template

app = Flask(__name__)

#For testing the Flask stuff, run flaskTutorial.py and search up 127.0.0.1:5000 -> That's the main page/default link.

#Routing -> Ties a url from a HTML website to  Python function. I think .route is the routing

#@ signifies a decorator - a decorator is a way to wrap a function and modify its behavior
#@app.route('/') #Routes to main page to website
#def index(): #Defines the main page
#    return 'This is the homepage' # This is what is returned when we head to the main(home page)

@app.route('/tuna')#Edit this later -> This basically sets a route to a another page from main. change the words behind the / to change the page you want to go to
def tuna():#Function doesn't have to be same name as HTML link
    return '<h1>This is a test<h1>'#Return values can run HTML, although you should never directly use HTML in the return method(using tags)

@app.route('/notprofile/<username>') # Anything inside the <> is a variable and can be treated as a parameter
def notprofile(username): #You should always pass the variable name into the parameter.
    return 'Hey there %s' % username
#As a note, while Strings only need to be written between <>, any other variables, like int, need to be written as <var:variable_name> EX: <int:post_id>

#There are two request methods(the .route() stuff), known as GET and POST. GET is more generally used/is default, POST is mostly only used when a page has a form
@app.route("/takis", methods=['GET', 'POST']) #The methods=['GET', 'POST'] allows for this app routing to use both GET and POST methods
def bacon():
    if request.method == 'POST': #Just an if function that checks if the page was called using a get or post method.
        return 'you are probably using POST'
    else:
        return 'You are probably using GET'
  
@app.route('/profile/<name>', methods=['GET'])
def otherProfile(name):
    return render_template("profile.html", substitute = name) #The render_template basically will have the webpage upload whatever html file have it render. In this case, it's profile.html
#The substitute=name is there to define what information needs to be displayed in the html layout. So the name is displayed.

#Routes multipe HTML pages to one function. So both / & /<user> are both links to the main page(Like how being signed in and being signed out have two different web pages)
@app.route('/')
@app.route('/<user>')
def index(user=None): #Defaults tbe user into being nothing.
    return render_template('user.html', user=user)

#How to load lists into a html webpage
@app.route('/shopping')
def shopping():
    food = ['Cheese', 'Tuna', 'Beef'] 
    return render_template('shoppinglist.html', food=food)

if __name__== "__main__": #This check make sure that the webserver runs only when this file is called directly
    app.run(debug=True) #This starts the app
    