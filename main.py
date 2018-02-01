from flask import Flask
from flask import request
from flask import make_response
import psycopg2
import pprint

app = Flask(__name__)

class Db():
    def __init__(self, db='storyboard', user='storyboard', host='localhost', password='igotSk1llz!'):
        print 'connecting to db:', db, 'with role:', user
        self.conn = psycopg2.connect(database=db, user=user)
        self.cur = self.conn.cursor()
        
    def connect_to_db():
        print "connecting to db..."
        conn_string = "dbname='storyboard', user='nishant', host='localhost', password=''"
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()

    def query(self, query, values = None):
        self.cur.execute(query, values)

    def fetch(self):
        return self.cur.fetchall()

    def close(self):
        self.cur.close()
        self.conn.close()


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
        query = 'INSERT into story(story, name) values(%s, %s)'
        db.query(query, (addition, 'Grant'))
        return '200'
    else:
        return '400'


