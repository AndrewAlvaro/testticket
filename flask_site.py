from flask import Flask, Blueprint, request, jsonify, render_template, redirect
from flask_paginate import Pagination, get_page_parameter, get_page_args
import os, requests, json
import random

site = Blueprint("site", __name__)

@site.route('/')
def home():
    return render_template('index.html')  # render a template

@site.route('/tickets')
def tickets():
    search = False
    response = requests.get("http://localhost:5000/ticketView")
    data = json.loads(response.text)
    
    per_page = 25

    page = request.args.get(get_page_parameter(), type=int, default=1)
    offset = (page - 1) * per_page

    datas = data[offset:offset + per_page]

    pagination = Pagination(page=page, per_page= per_page, total=len(data), search=search, record_name='data', css_framework='bootstrap4')

    return render_template('tickets.html', tickets = datas, pagination = pagination)
    #return render_template('tickets.html', tickets = data)

@site.errorhandler(500)
def could_not_auth(e):
    
    return render_template('500.html'), 500

@site.route('/singleTicket/<id>')
def singleTickets(id):
    response = requests.get("http://localhost:5000/api/ticketID/" + id)
    data = json.loads(response.text)
    return render_template('ticketid.html', ticket = data)