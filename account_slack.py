from jbowens_common import parameter
import requests
import json

def AccountCreation(Employee):
    
    print(json.dumps(secrets_manager.get_secret("servicedesk/slack", "us-west-2")))
    secret = json.dumps(secrets_manager.get_secret("servicedesk/slack", "us-west-2"))

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    body = {
        "email": Employee.WorkEmail, "first_name": Employee.FirstName, "last_name": Employee.LastName
    }

    response = requests.post('https://jbowensco.slack.com/api/users.admin.invite', headers=headers, data=body)
    print(response.text)

def GetUsers():

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': "Bearer " + secrets_manager.get_secret("servicedesk/slack", "us-west-2")
    }

    print(requests.get('https://slack.com/api/users.list', headers=headers))