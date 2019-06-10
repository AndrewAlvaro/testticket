from zenpy import Zenpy
from flask import Flask, request, jsonify, render_template
import os, requests, json
from flask_api import api
from flask_site import site


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))


app.register_blueprint(site)
app.register_blueprint(api)

if __name__ == "__main__":
    app.run(host = "0.0.0.0")
