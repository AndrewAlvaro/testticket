from flask import Flask, Blueprint, request, jsonify, render_template
from zenpy import Zenpy
import os, requests, json
import datetime


api = Blueprint("api", __name__)


# Zenpy API token
creds = {
    'email' : 'andrew.alvaro10@gmail.com',
    'token' : 'hHp0kBgaMfdtDGwKYJMLSfCNBkXH5r9zznYoiOjP',
    'subdomain' : 'testticket2019'
}

zenpy_client = Zenpy(**creds)

@api.route("/ticketView", methods = ["GET"])
def showTicket():
    
    ticketz = []
    for datas in zenpy_client.tickets():
        data = datas.to_dict()
        tickets = dict()
        
        tickets['id'] = data['id']
        tickets['status'] = data['status']
        tickets['requestID'] = data['requester_id']
        tickets['assignID'] = data['assignee_id']
        tickets['subject'] = data['subject']
        tickets['description'] = data['description']
        tickets['tags'] = data['tags']
        
        ticketz.append(tickets)

    return jsonify(ticketz)
    

@api.route("/api/ticketID/<id>")
def showSingleTicket(id):
    ticket = zenpy_client.tickets(id=id)
    data = ticket.to_dict()

    id = data['id']
    status = data['status']
    requestID = data['requester_id']
    assignID = data['assignee_id']
    subject = data['subject']
    description = data['description']
    tags = data['tags']
    created_at = data['created_at']
    updated_at = data['updated_at']

    tickets = {"id": id, "status": status, "requestID": requestID, "assignID": assignID, "subject": subject, "description": description, "tags": tags, "created_at": created_at, "updated_at": updated_at}

    return jsonify(tickets)
