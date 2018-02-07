
import psycopg2

class Db():
    def __init__(self, db='storyboard', user='storyboard', host='localhost', password=''):
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

    def insert_story(self, values = None): 
        query = 'INSERT into story(story, name) values(%s, %s)'
        db.query(query, values)

    def commit(self):
        self.conn.commit()

    def fetch(self):
        return self.cur.fetchall()

    def close(self):
        self.cur.close()
        self.conn.close()


