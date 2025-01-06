import PySimpleGUI as sg

personList = []
def update_people():
    personList.clear()
    for items in range(len(Person.data)): # assigns all items a number
        personList.append([]) # Create 2d list
        personList[items].append(Person.data[items].name) 
        personList[items].append(Person.data[items].salary) 
        personList[items].append(Person.data[items].phoneNo) 
        personList[items].append(Person.data[items].address)

class Person:
    data = []
    def __init__(self,name,salary,phoneNo,address):
        self.name = name
        self.salary = salary
        self.phoneNo = phoneNo
        self.address = address
        Person.data.append(self)

JohnPerson = Person('John',3123,4013803,'21 Jump St.')

update_people()