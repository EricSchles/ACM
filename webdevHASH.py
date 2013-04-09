"""

This simple website takes in your journal entries, stores it for you
and allows you to edit it.

This website is in flask.

Stores data as a hash map
"""

from flask import Flask



class dataStore:
    def __init__(self):
        self.hashmap = {}

    def get(self):
        """used to get an item in the map"""
        
    def add(self):
    """used to add an item in the map"""
    
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
