"""

This simple website takes in your journal entries, stores it for you
and allows you to edit it.

This website is in flask.

Stores data as a hash map
"""

#all the imports
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash
import pickle

#configuration
DATABASE = ''
DEBUG = False
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

#create our little application
app = Flask(__name__)
app.config.from_object(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/get")
def get_value():
    return g.data.get(request.args.get('key',''))

@app.route("/put")
def put_value():
    return g.data.add({request.args.get('key'): request.args.get('value')})

class dataStore:
    def __init__(self):
        self.hashmap = {} #instantiates a hashmap

    def get(self, key):
        """used to get an item in the map"""
        return self.hashmap[key]

    def has_key(self, key):
        """Check if a key is associated with a value in the map"""
        return self.hashmap.has_key(key)

    def add(self,key_value):
        """used to add an item in the map, must be of the form {key:value}"""
        self.hashmap.update(value)

    def remove(self,key):
        """used to remove an item from the map"""
        del self.hashmap[key]

    def isEmpty(self):
        """checks if hashmap is empty, returns a boolean"""
        return self.hashmap != {}

    def makeEmpty(self):
        """makes the hashmap empty, if it isn't already"""
        if not isEmpty():
            self.hashmap = {}

@app.before_request
def before_request():
    """Initializes a datastore for this session"""
    g.data = dataStore()
    g.data.hashmap = pickle.load(open("dataStore","r"))
 
@app.teardown_request
def teardown_request(exception):
    """sends data to a persistent file, closes connection"""
    if not g.data.isEmpty():
        fileobject = open("dataStore", "w")
        pickle.dump(g.data.hashmap, fileobject)
        #sends the datastructure to a file on teardown
        #to load simply do x = pickle.load(fileobject)

if __name__ == '__main__':
    app.debug = True
    app.run()
