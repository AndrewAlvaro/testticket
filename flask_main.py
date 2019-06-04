from zenpy import Zenpy
from flask import Flask, request, jsonify, render_template
from flask_marshmallow import Marshmallow
import os, requests, json
from flask_api import api
from flask_site import site

# Zenpy API token
creds = {
    'email' : 'andrew.alvaro10@gmail.com',
    'token' : 'hHp0kBgaMfdtDGwKYJMLSfCNBkXH5r9zznYoiOjP',
    'subdomain': 'https://testticket2019.zendesk.com'
}

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Default
zenpy_client = Zenpy(**creds)

app.register_blueprint(site)
app.register_blueprint(api)

if __name__ == "__main__":
    app.run(host = "0.0.0.0")
