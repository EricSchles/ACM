"""

This simple website takes in your journal entries, stores it for you
and allows you to edit it.

This website is in flask.

Stores data as a hash map
"""

from flask import Flask



class dataStore:
    def __init__(self):
        self.hashmap = {} #instantiates a hashmap
        

    def get(self, key):
        """used to get an item in the map"""
        return self.hashmap[key]
        
    def add(self,value):
        """used to add an item in the map, must be of the form {key:value}"""
        self.hashmap.update(value)

    def remove(self):
        """used to remove an item from the map"""
        



#basic idea, fix this....
@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('insert into entries (title, text) values (?, ?)',
                 [request.form['title'], request.form['text']])
    db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))
