import datetime as dt
import numpy as np
import pandas as pd
from flask import Flask, jsonify
import json
from sqlHelper import SQLHelper

#######################################################

app = Flask(__name__)

sqlHelper = SQLHelper()

@app.route("/")
def home():
    print("Client requested the home page from the server")
    return("<h1>Welcome to my home page!</h1>")

@app.route("/api/v1.0/precipitation")
def get_test_measurements():
    data = sqlHelper.get_test_precepitation()
    return jsonify(json.loads(data.to_json(orient="records")))

@app.route("/api/v1.0/stations")
def get_station():
    data = sqlHelper.get_station()
    return jsonify(json.loads(data.to_json(orient="records")))

@app.route("/api/v1.0/tobs")
def get_tobs_userQuery():
data = sqlHelper.get_station()
    return jsonify(json.loads(data.to_json(orient="records")))

@app.route("/api/v1.0/tobs")
@app.route("/api/v1.0/tobs/<start>")
@app.route("/api/v1.0/tobs/<start>/<end>")
def get_tobs_userQuery(start=None, end = None):
    
    data = sqlHelper.get_tobs_userQuery(start, end)
    return jsonify(json.loads(data.to_json(orient="records")))


if __name__ == "__main__":
    app.run(debug=True)
