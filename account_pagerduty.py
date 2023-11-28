from jbowens_common import parameter
from employee import Employee
import requests
import sys
import json

def AccountCreation(Employee):

    headers = {
        'Accept': 'application/application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Token token=rJPi9by3i5ZqmdgXJC9w'
    }

    body = {
        "user": {
            "type": "user",
            "name": Employee.DisplayName,
            "email": Employee.SecondaryEmail,
            "role": "user",
            "job_title": Employee.JobTitle
        }
    }

    requests.post('https://api.pagerduty.com/users', headers=headers, data=json.dumps(body))