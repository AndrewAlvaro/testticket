from flask import Flask, Blueprint, request, jsonify, render_template
from zenpy import Zenpy
import os, requests, json
import datetime


api = Blueprint("api", __name__)


# Zenpy API token
creds = {
    'email' : 'andrew.alvaro10@gmail.com',
    'token' : 'hHp0kBgaMfdtDGwKYJMLSfCNBkXH5r9zznYoiOjP',
    'subdomain': 'testticket2019'
}


zenpy_client = Zenpy(**creds)

@api.route("/ticketView", methods = ["GET"])
def showTicket():

    for ticket in zenpy_client.tickets():
        data = ticket.to_dict()
    
    id = data['id']
    status = data['status']
    requestID = data['requester_id']
    assignID = data['assignee_id']
    subject = data['subject']
    description = data['description']
    tags = data['tags']

    tickets = {"id": id, "status": status, "requestID": requestID, "assignID": assignID, "subject": subject, "description": description, "tags": tags}

    return jsonify(tickets)

