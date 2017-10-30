#!flask/bin/python
from flask import Flask, render_template, jsonify
import datetime
import mysql.connector

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('main.html')


@app.route('/api/getMeasures', methods=['GET'])
def get_measures():
    cnx = mysql.connector.connect(user='root', database='xx', password='xx')

    cursor = cnx.cursor()
    cursor.execute('select ts, measure from measurement');
    rows = cursor.fetchall()

    returnlist = list()
    for ts, measure in rows:
        timestamp = ts.strftime('%Y-%m-%dT%H:%M:%S')
        measurement = measure
        measureobject = (timestamp, measurement)
        returnlist.append(measureobject)

    cursor.close()
    cnx.close()

    return jsonify(returnlist)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

