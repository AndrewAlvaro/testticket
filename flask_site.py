from flask import Flask, Blueprint, request, jsonify, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os, requests, json
import random

site = Blueprint("site", __name__)

@site.route('/')
def home():
    return render_template('index.html')  # render a template

@site.route('/tickets')
def tickets():
    response = requests.get("http://localhost:5000/ticketView")
    data = json.loads(response.text)
    return render_template('removebooks.html', tickets = data)