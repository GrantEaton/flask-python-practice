import psycopg2
import yaml

class Db():
    """
    Constructor. Connects to db
    params:
        db_name (string): name of db to connect
        bd_identifier (string): the identifier used in the .creds.yml file to group credentials
    """
    def __init__(self, db_name='sfmaps', db_identifier='AWS'):
        conf = yaml.load(open('.creds.yml'))
        host = conf[db_identifier]['HOST']
        port = conf[db_identifier]['PORT']
        user = conf[db_identifier]['USER']
        password = conf[db_identifier]['PASSWORD']

        print 'connecting to ',db_identifier, 'db:', db_name, 'with role:', user 
        conn_string = "host="+host+" port="+port+" dbname=" +db_name+" user="+user+" password="+password
        self.conn = psycopg2.connect(conn_string)
        self.cur = self.conn.cursor()
    """ 
    Queries the db.
    params:
        query (string): the query string 
        values (list of strings): values to be inserted into query string
    """
    def query(self, query, values = None):
        self.cur.execute(query, values)

    """
    Custom func for story. Delete after db re-purpose for postgis mapping
    """
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


