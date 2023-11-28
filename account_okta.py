from jbowens_common import parameter
import requests
import sys
import json

def AccountCreation(Employee):

    print(secrets_manager.get_secret("servicedesk/okta", "us-west-2"))  


    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'SSWS  ' + secrets_manager.get_secret("servicedesk/okta", "us-west-2")
    }

    body = {
        "profile": {"firstName": Employee.FirstName, "lastName": Employee.LastName, "login": Employee.WorkEmail, "email": Employee.WorkEmail, "title": Employee.JobTitle,
        "userType": Employee.EmployeeType, "organization": "jbowens", "division": Employee.Division, "department": Employee.Department, "manager": Employee.ManagerEmail,
        "secondEmail": Employee.SecondaryEmail
        },
        "credentials": {"password" : {"value": Employee.Password}},
        "groupIds": Employee.OktaGroups
    }

    response = requests.post('https://jbowens.okta.com/api/v1/users?activate=true&nextLogin=changePassword', headers=headers, data=json.dumps(body))
    print(response.text)