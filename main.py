from flask import Flask
from flask import request
from flask import make_response
from db import Db
import pprint

app = Flask(__name__)


if __name__ == "__main__":
    print "Run using `Flask run` instead."    


# Queries to be modified to generate FeatureCollection - currently just returns geometry

@app.route("/api/map")
def map():
    """
    GET method to retrieve map geometry
    :return: GeoJSON FeatureCollection of map geometry
    """

    db = Db()
    query = "SELECT ST_AsGeoJSON(wkb_geometry) from public.map"
    db.query(query)
    print "Returns map data as GeoJSON feature collection"
    rows = db.fetch()
    db.close()
    return rows


@app.route("/api/streets")
def streets():
    """
    GET method to retrieve streets geometry
    :return: GeoJSON FeatureCollection of streets geometry
    """

    query = "SELECT ST_AsGeoJSON(wkb_geometry) from public.streets"
    db = Db()
    db.query(query)
    print "Returns streets as GeoJSON feature collection"
    rows = db.fetch()
    db.close()
    return rows

# Returns the arteries geometry as a GeoJSON feature collection
@app.route("/api/arteries")
def arteries():
    """
    GET method to retrieve arteries geometry
    :return: GeoJSON FeatureCollection of arteries geometry
    """

    query = "SELECT ST_AsGeoJSON(wkb_geometry) from public.arteries"
    db = Db()
    db.query(query)
    print "Returns arteries as GeoJSON feature collection"
    rows = db.fetch()
    db.close()
    return rows


@app.route("/api/neighborhoods")
def neighborhoods():

    """
    GET method to retrieve neighborhoods geometry
    :return: GeoJSON FeatureCollection of neighborhoods geometry
    """

    query = "SELECT ST_AsGeoJSON(wkb_geometry) from public.neighborhoods"
    db = Db()
    db.query(query)
    print "Returns neighborhoods as GeoJSON feature collection"
    rows = db.fetch()
    db.close()
    return rows


@app.route("/api/freeways")
def freeways():
    """
    GET method to retrieve freeways geometry
    :return: GeoJSON FeatureCollection of freeways geometry
    """

    query = "SELECT ST_AsGeoJSON(wkb_geometry) from public.freeways"
    db = Db()
    db.query(query)
    print "Returns freeways as GeoJSON feature collection"
    rows = db.fetch()
    db.close()
    return rows




