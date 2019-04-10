import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


#################################################
# Database Setup
#################################################

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///hot.sqlite" 
db = SQLAlchemy(app)

# Create our database model
class Climate(db.Model):
    __tablename__ = 'hot'

    index = db.Column(db.Integer, primary_key=True)
    Declaration_year = db.Column(db.String)
    Disaster_Type = db.Column(db.String)
    Disaster_Count = db.Column(db.Integer)
    Avg_Temp = db.Column(db.String)

    def __repr__(self):
        return '<Emoji %r>' % (self.index)


@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

# @app.route("/")
# def c3_graph():

#     return()

@app.route("/climate_data")
def climate_data():

    results = db.session.query(Climate.Declaration_year, Climate.Disaster_Type, Climate.Disaster_Count, Climate.Avg_Temp).all()

    
    return jsonify(results)





if __name__ == "__main__":
    app.run()