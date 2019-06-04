from flask import Flask, Blueprint, request, jsonify, render_template, redirect
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
    return render_template('tickets.html', tickets = data)