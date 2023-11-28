from jbowens_common import parameter
import requests
import sys
import json

def AccountCreation(Employee):

    headers = {
        'Authorization': 'token  ',
        'Accept': 'application/vnd.github.dazzler-preview+json'
    }

    body = {
        "email": Employee.WorkEmail,
        "role": "direct_member",
        "team_ids": [] #This should be updated with logic to determine what teams
    }

    requests.post('https://api.github.com/orgs/jbowens/invitations', headers=headers, data=json.dumps(body))