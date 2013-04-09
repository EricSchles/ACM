"""

This simple website takes in your journal entries, stores it for you
and allows you to edit it.

This website is in flask.

Stores data as a hash map
"""

#all the imports
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash

#configuration
DATABASE = ''
DEBUG = False
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

#create our little application
app = Flask(__name__)
app.config.from_object(__name__)



class dataStore:
    def __init__(self):
        self.hashmap = {} #instantiates a hashmap
        

    def get(self, key):
        """used to get an item in the map"""
        return self.hashmap[key]
        
    def add(self,key_value):
        """used to add an item in the map, must be of the form {key:value}"""
        self.hashmap.update(value)

    def remove(self,key):
        """used to remove an item from the map"""
        del self.hashmap[key]

    def isEmpty(self):
        return self.hashmap != {}:
            
    def makeEmpty(self):
        if not isEmpty():
            self.hashmap = {}


@app.before_request
def before_request():
    data = dataStore()
 
@app.teardown_request
def teardown_request(exception):
    
    

if __name__ == '__main__':
    app.run()
