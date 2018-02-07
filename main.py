from flask import Flask
from flask import request
from flask import make_response
from db import Db
import pprint

app = Flask(__name__)

db = Db(); 


if __name__ == "__main__":
    print "Run using `Flask run` instead."    

def get_story():
    db.query("SELECT * from story;");
    records = db.fetch()
    return records

""" Routing Stuff """
@app.route('/')
def display_story():
    story = ''
    for post in get_story():
        story += post[1]
    return story

@app.route('/publish', methods=['GET', 'POST'])
def add_to_story():
    if request.method == 'POST':
        addition = request.form['addition']
        db.insert_story((addition, 'Grant'))
        db.commit()
        return '200'
    else:
        return '400'


