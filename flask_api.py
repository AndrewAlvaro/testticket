from flask import Flask, Blueprint, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from zenpy import Zenpy
import os, requests, json



api = Blueprint("api", __name__)
db = SQLAlchemy()

creds = {
    'email' : 'andrew.alvaro10@gmail.com',
    'token' : 'hHp0kBgaMfdtDGwKYJMLSfCNBkXH5r9zznYoiOjP',
    'subdomain': 'testticket2019'
}


zenpy_client = Zenpy(**creds)

class Ticket(db.Model):
    __tablename__ = "Ticket"
    id = db.Column(db.Integer, primary_key = True)
    requestID = db.Column(db.Text)
    assignID = db.Column(db.Text)
    subject = db.Column(db.Text)
    description = db.Column(db.Text)

    def __init__(self, id, requestID, assignID, subject, description):
        self.id = id
        self.requestID = requestID
        self.assignID = assignID
        self.subject = subject
        self.description = description

@api.route("/ticketView", methods = ["GET"])
def showTicket():
    for ticket in zenpy_client.tickets():
        data = ticket

    id = data['id']
    requestID = data['requester_id']
    assignID = data['assignee_id']
    subject = data['subject']
    description = data['description']

    tickets = Ticket(id = id, requestID = requestID, assignID = assignID, subject = subject, description = description)

    return jsonify(tickets)