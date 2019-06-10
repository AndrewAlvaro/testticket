import unittest
from flask_api import api, zenpy_client
from flask_site import site
from flask_main import app
from flask import Flask, Blueprint, request, jsonify, render_template, redirect
import os, requests, json

class TestFlask(unittest.TestCase):
    '''''''''''''''''''''
    ' Setup and teardown'
    '''''''''''''''''''''

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass
    
    '''''''''''''''''''''
    '       Tests       '
    '''''''''''''''''''''

    def retrieveData(self):
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

            json_ticketz = json.dumps(ticketz)
            list_ticketz = json.loads(json_ticketz)
            
        return list_ticketz

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    def test_ticket_page(self):
        response = self.app.get('/tickets', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_ticket_view_page(self):
        response = self.app.get('/singleTicket/1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_retrieveTickets(self):
        with app.app_context():
            response = requests.get("http://localhost:5000/ticketView")
            data = json.loads(response.text)
            
            self.assertListEqual(self.retrieveData(), data)
    
    def test_retrieveSingleTicket(self):
        id = "1"

        response = requests.get("http://localhost:5000/api/ticketID/" + id)
        data = json.loads(response.text)

        self.assertTrue(data['id'] == 1)
        self.assertFalse(data['id'] == 2)



if __name__ == "__main__":
    unittest.main()