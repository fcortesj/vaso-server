"""
This module contains the creation of the flask app and the Restful api.

It is created the configurartions of the data base in MongoDB so connection is established.
"""

from flask import Flask
from flask_restful import Api
from flask_pymongo import PyMongo

app = Flask(__name__)
api = Api(app)

app.config["MONGO_DBNAME"] = "ClusterTelematica"
app.config["MONGO_URI"] = "mongodb+srv://fcortesj:fcjCMF43*@clustertelematica-kklis.mongodb.net/test?retryWrites=true&w=majority"

mongo = PyMongo(app)
