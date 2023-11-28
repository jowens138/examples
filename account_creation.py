import csv
from jbowens_common import parameter
from employee import Employee
import account_okta
import account_slack
import account_github
import account_pagerduty
 
#Define variables
employees = []

#Read employee information from csv file
with open('new_hire.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    
    #skip csv header
    next(readCSV)
    
    #create Employee objects from csv    
    for row in readCSV:
        employees.append(Employee(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))

    #Use Employee object(s) to create accounts
    for Employee in employees:

        print("User: " + Employee.WorkEmail)
        print("Password: " + Employee.Password)
        
        #Call Okta Account Creation
        account_okta.AccountCreation(Employee)
        #print("Okta account created")

        #Call Slack Account Creation
        account_slack.AccountCreation(Employee)

        #Call Github Account Creation
        #account_github.AccountCreation(Employee)
        
        #Call Pagerduty Account Creation
        #account_pagerduty.AccountCreation(Employee)
