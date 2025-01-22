# Name: Aiden Deane
# Title: Universal Business Portal - employee_service
# Date: Final Commit 22 Jan 2025
# Description: Writes and saves data to employee_log.py, and acts as a staging area for all people classes.


# This layout is almost exactly the same as database_array.py All relevant annotations are there!

import os
from config.employee_log import *

def load_data():
    for people in range(len(empList)):
        Person(empList[people][0],empList[people][1],empList[people][2],empList[people][3])

personList = []
def update_people():
    personList.clear()
    for people in range(len(Person.data)): # assigns all items a number
        personList.append([]) # Create 2d list
        personList[people].append(Person.data[people].name) 
        personList[people].append(Person.data[people].salary) 
        personList[people].append(Person.data[people].phoneNo) 
        personList[people].append(Person.data[people].address)
    #            ^^^^^                   ^^^^^
    #   Output list index       input list index
        filepath = os.path.join(f"{os.getcwd()}/config/employee_log.py")
        classLog = open(filepath,'a')
        classLog.truncate(0) # Clear to rebuild list
        classLog.write(f'empList = {personList}') 
        classLog.close()

class Person:
    data = []
    def __init__(self,name,salary,phoneNo,address):
        self.name = name
        self.salary = salary
        self.phoneNo = phoneNo
        self.address = address
        Person.data.append(self)


load_data()

update_people()
