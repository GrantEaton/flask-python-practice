from flask import Flask
from flask import request
from flask import make_response
from db import Db
import pprint

app = Flask(__name__)

db = Db()

if __name__ == "__main__":
    print "Run using `Flask run` instead."    

@app.route("/api/map")
def map():
    print "Returns map data as GeoJSON feature collection"

@app.route("/api/streets")
def streets():
    print "Returns streets as GeoJSON feature collection"

@app.route("/api/arteries")
def arteries():
    print "Returns arteries as GeoJSON feature collection"

@app.route("/api/neighborhoods")
def neighborhoods():
    print "Returns neighborhoods as GeoJSON feature collection"



