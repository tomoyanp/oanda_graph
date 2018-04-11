from flask import Flask
from flask import render_template, jsonify, url_for, Response
import json
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/get_json')
def get_json():
    data = [
        {"Date": "9-Jun-14"  ,"Open": "62.40", "High": "63.34","Low": "61.79", "Close": "62.88", "Volume": "37617413"},
        {"Date": "6-Jun-14"  ,"Open": "63.37", "High": "63.48","Low": "62.15", "Close": "62.50", "Volume": "42442096"},
        {"Date": "5-Jun-14"  ,"Open": "63.66", "High": "64.36","Low": "62.82", "Close": "63.19", "Volume": "47352368"},
        {"Date": "4-Jun-14"  ,"Open": "62.45", "High": "63.59","Low": "62.07", "Close": "63.34", "Volume": "36513991"},
        {"Date": "3-Jun-14"  ,"Open": "62.62", "High": "63.42","Low": "62.32", "Close": "62.87", "Volume": "32216707"},
        {"Date": "2-Jun-14"  ,"Open": "63.23", "High": "63.59","Low": "62.05", "Close": "63.08", "Volume": "35995537"},
        {"Date": "30-May-14" ,"Open": "63.95", "High": "64.17","Low": "62.56", "Close": "63.30", "Volume": "45283577"},
        {"Date": "29-May-14" ,"Open": "63.84", "High": "64.30","Low": "63.51", "Close": "63.83", "Volume": "42699670"},
        {"Date": "28-May-14" ,"Open": "63.39", "High": "64.14","Low": "62.62", "Close": "63.51", "Volume": "47795088"}
    ]

    print data
    print "==========================================="
#    data = jsonify(data)
    data = json.dumps(data)
    print data
    response = Response(response=data, status=200, mimetype="application/json")
    return response


if __name__ == "__main__":
    app.run(debug=True)
