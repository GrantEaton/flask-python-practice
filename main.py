from flask import Flask
from flask import request
from flask import make_response, Response
from db import Db
import pprint
import json

app = Flask(__name__)


if __name__ == "__main__":
    print "Run using `Flask run` instead."

db = None

@app.before_request
def open_db():
    """
    Open the connection to DB before every request
    :return:
    """
    global db
    db = Db()

@app.teardown_appcontext
def close_db(exception):
    """
    Close the DB and flush any other resources
    :param exception: any exception that might have occurred
    :return:
    """
    global db
    if exception is not None:
        print exception
    if db is not None:
        db.close()

# Queries to be modified to generate FeatureCollection - currently just returns geometry

@app.route("/api/map")
def map():
    """
    GET method to retrieve map geometry
    :return: GeoJSON FeatureCollection of map geometry
    """
    global db
    query = """SELECT row_to_json(fc)
    FROM ( SELECT 'FeatureCollection' As type, array_to_json(array_agg(f)) As features
    FROM (SELECT 'Feature' As type
       , ST_AsGeoJSON(map.wkb_geometry)::json As geometry
       , row_to_json((SELECT l FROM (SELECT neighborho,street,zip_code,district,accepted,jurisdicti,streetname) As l
         )) As properties
      FROM map ) As f )  As fc;"""
    db.query(query)
    print "Returns map data as GeoJSON feature collection"
    rows = db.fetch()
    return Response(json.dumps(rows),mimetype="application/json")


@app.route("/api/streets")
def streets():
    """
    GET method to retrieve streets geometry
    :return: GeoJSON FeatureCollection of streets geometry
    """
    global db
    query = """SELECT row_to_json(fc)
    FROM ( SELECT 'FeatureCollection' As type, array_to_json(array_agg(f)) As features
    FROM (SELECT 'Feature' As type
       , ST_AsGeoJSON(st.wkb_geometry)::json As geometry
       , row_to_json((SELECT l FROM (SELECT street,zip_code,accepted,district,jurisdicti,streetname) As l
         )) As properties
      FROM streets as st ) As f )  As fc;"""
    db.query(query)
    print "Returns streets as GeoJSON feature collection"
    rows = db.fetch()
    return Response(json.dumps(rows),mimetype="application/json")

# Returns the arteries geometry as a GeoJSON feature collection
@app.route("/api/arteries")
def arteries():
    """
    GET method to retrieve arteries geometry
    :return: GeoJSON FeatureCollection of arteries geometry
    """
    global db
    query = """SELECT row_to_json(fc)
 FROM ( SELECT 'FeatureCollection' As type, array_to_json(array_agg(f)) As features
 FROM (SELECT 'Feature' As type
    , ST_AsGeoJSON(ar.wkb_geometry)::json As geometry
    , row_to_json((SELECT l FROM (SELECT streetname) As l
      )) As properties
   FROM arteries as ar ) As f )  As fc;"""
    db.query(query)
    print "Returns arteries as GeoJSON feature collection"
    rows = db.fetch()
    return Response(json.dumps(rows),mimetype="application/json")


@app.route("/api/neighborhoods")
def neighborhoods():

    """
    GET method to retrieve neighborhoods geometry
    :return: GeoJSON FeatureCollection of neighborhoods geometry
    """
    global db
    query = """SELECT row_to_json(fc)
    FROM ( SELECT 'FeatureCollection' As type, array_to_json(array_agg(f)) As features
    FROM (SELECT 'Feature' As type
       , ST_AsGeoJSON(nhoods.wkb_geometry)::json As geometry
       , row_to_json((SELECT l FROM (SELECT neighborho) As l
         )) As properties
      FROM neighborhoods as nhoods ) As f )  As fc;"""
    db.query(query)
    print "Returns neighborhoods as GeoJSON feature collection"
    rows = db.fetch()
    return Response(json.dumps(rows),mimetype="application/json")


@app.route("/api/freeways")
def freeways():
    """
    GET method to retrieve freeways geometry
    :return: GeoJSON FeatureCollection of freeways geometry
    """
    global db
    query = """SELECT row_to_json(fc)
 FROM ( SELECT 'FeatureCollection' As type, array_to_json(array_agg(f)) As features
 FROM (SELECT 'Feature' As type
    , ST_AsGeoJSON(fr.wkb_geometry)::json As geometry
    , row_to_json((SELECT l FROM (SELECT streetname) As l
      )) As properties
   FROM freeways as fr ) As f )  As fc;"""
    db.query(query)
    print "Returns freeways as GeoJSON feature collection"
    rows = db.fetch()
    return Response(json.dumps(rows),mimetype="application/json")





