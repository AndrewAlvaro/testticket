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

@site.errorhandler(500)
def could_not_auth(e):
    
    return render_template('500.html'), 500

@site.route('/singleTicket/<id>')
def singleTickets(id):
    response = requests.get("http://localhost:5000/api/ticketID/" + id)
    data = json.loads(response.text)
    return render_template('ticketid.html', ticket = data)