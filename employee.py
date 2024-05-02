from jbowens_common import parameter
import string
import random
# employee class
class Employee:

    #variables passed from main
    EmployeeID=""
    FirstName=""
    LastName=""
    DisplayName=""
    SecondaryEmail=""
    JobTitle=""
    EmployeeType=""
    ManagerEmail=""
    Department=""
    Office=""

    #variables created by employee class
    AccountName=""
    WorkEmail=""
    Password=""

    GoogleGroups=[]
    OktaGroups=[]
    LastPassGroups=[]

    #initialize an Employee object
    def __init__ (self, first, last, email, title, EmpType, manager, department, office, division):  
        #self.EmployeeID=EmpID - Removed until we get Employ IDs worked out
        self.FirstName=first
        self.LastName=last
        self.SecondaryEmail=email
        self.JobTitle=title
        self.EmployeeType=EmpType
        self.ManagerEmail=manager
        self.Department=department
        self.Office=office
        self.Division=division

        self.GoogleGroups=[]
        self.LastPassGroups=[]
        self.OktaGroups=[]

        #Create username based on Lowercase First Name + Last Name
        self.Username = self.FirstName.lower() + "." + self.LastName.lower()

        #Create Display Name from First Name and Last Name
        self.DisplayName = self.FirstName + " " + self.LastName

        #Create email address based on username + devision (jbowens.me, howstuffworks.com, etc.)
        self.WorkEmail = self.Username + "@" + self.Division.lower() + ".com"

        #Call GeneratePassword
        self.GeneratePassword()

        #Call AddGoogleGroups
        self.AddGoogleGroups()

        #Call AddOktaGroups - Removed, Okta has internal logic for this and the API didn't like the formatting - "groupIds": ["Group 1 ID", "Group 2 ID"]
        #self.AddOktaGroups()

        #Call AddLastPassGroups
        self.AddLastPassGroups()

        #Call AddAddress - Street, City, State, Zip, Country


    #Generate a random password
    def GeneratePassword(self, size = 6, chars=string.ascii_letters + string.digits + "!" + "$" + "&" + "#" + "<" + "."):
        self.Password = "1rP!" + (''.join(random.choice(chars) for _ in range(size)))

    #Create list of G Suite Groups based on department and office
    def AddGoogleGroups(self):
        if self.Office == "Venice":
            self.GoogleGroups.append("venice@jbowens.me")
        elif self.Office == "Bellevue":
            self.GoogleGroups.append("bellevue@jbowens.me")
        elif self.Office == "Atlanta":
            self.GoogleGroups.append("atlanta@jbowens.me")           
        elif (self.Office == "Guelph") and (self.Division == "1"):
            self.GoogleGroups.append("employees@jbowens.me", )
            self.GoogleGroups.append("one@jbowens.me")
        elif (self.Office == "Guelph") and (self.Division == "2"):
            self.GoogleGroups.append("two@jbowens.me")

    #Create list of LastPass groups based on department
    def AddLastPassGroups(self):

        #Append Office Group(s)
        if self.Office == "Bellevue":
            self.LastPassGroups.append("jbowens-Bellevue_All")

        #Append Department Group(s)
        if self.Department == "DevOps":
            self.LastPassGroups.append("jbowens-Helpdesk")
            self.LastPassGroups.append("jbowens-DevOps")
        elif self.Department == "HR":
            self.LastPassGroups.append("jbowens-HR")
        elif self.Department == "Search Engineering":
            self.LastPassGroups.append("jbowens-SearchEngineering")
        elif self.Department == "Social Publishing":
            self.LastPassGroups.append("jbowens-SocialPub")
        elif self.Department == "Product":
            self.LastPassGroups.append("jbowens-Product")
        elif self.Department == "ETL":
            self.LastPassGroups.append("jbowens-ETL")
