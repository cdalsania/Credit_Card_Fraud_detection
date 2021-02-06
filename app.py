###############################################
# Import Dependencies
###############################################

from flask import Flask, render_template, jsonify, request
from os import environ
import json
import os
from config import CSV_FILE_URL
import pandas as pd

###############################################
# Flask Setup & Access Environ Variables
###############################################

# Creating new application of the flask module
app = Flask(__name__)

csv_file_path = environ.get('CSV_FILE_PATH') or CSV_FILE_URL

###############################################
# Flask Routes
###############################################

# Routes that will render html templates
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/navbar')
def navbar():
    return render_template('navbar.html')

@app.route('/footer')
def footer():
    return render_template('footer.html')

@app.route('/data')
def data():
    return render_template('data.html')

@app.route('/research')
def research():
    return render_template('research.html')

@app.route('/predictions')
def predictions():
    return render_template('predictions.html')

@app.route('/conclusions')
def conclusions():
    return render_template('conclusions.html')

###############################################
# Run the Flask Application
###############################################

# Spin-up the Flask Application
if __name__ == "__main__":
    app.run(debug=True)