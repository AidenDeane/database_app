import PySimpleGUI as sg
from database_array import *
from pos_service import *
from employee_service import *


passwordLayout = [
    [sg.Text('Please enter your password!')],
    [sg.Input(key='-pw-'), sg.Button('OK')] # key -pw- acts as identifier for events
    ]
passwordPage = sg.Window('Password',passwordLayout)

homepageLayout = [ 
    [sg.Push(), sg.Text("Welcome to the Universal Business Portal!",font=('Arial',20)), sg.Push()]
     ]
#homepage = sg.Window('Home', homepageLayout, size=(720,720))

inventoryLayout = [
    [sg.Push(), sg.Text("DATABASE SERVICE"), sg.Push()],
    [sg.Table(values=dataList,headings=['PRODUCT NAME','RETAIL PRICE','IN INVENTORY','ITEM ID'],expand_x=True,expand_y=True,key='--database--')],
    [sg.Push(),sg.Text('PRODUCT ENTRY'),sg.Push()],
    [sg.Text(text="Product Name",size=27),sg.Text(text='Retail Price',size=27),sg.Text(text='In Inventory',size=27),sg.Text(text='Product ID',size=27)],
    [sg.Input(key='-prodName-',size=27),sg.Input(key='-prodRP-',size=27),sg.Input(key='-inInv-',size=27),sg.Input(key='-prodID-',size=27)],
    [sg.Button("Add Item",key='-invAdd-')]
]
#inventoryPage = sg.Window('Inventory',inventoryLayout, size=(720,720))

posLayout = [ # piece of shit layout
    [sg.Push(), sg.Text("POINT OF SALES SERVICE"), sg.Push()],
    [sg.Text(text='Item Name:',font=10,size=50),sg.Text(text='Amount Bought:',font=10,size=50)],
    [sg.Input(key='-checkoutName-',size=50),sg.Input(key='-checkoutAmnt-',size=50),sg.Button(button_text='Enter',key='-posCheck-',size=5)],
    [sg.Text(text='',key='-posName-',font=('Arial',20),size=27),sg.Text(text='',key='-posInv-',font=('Arial',20),size=27)],
    [sg.Text('CURRENT TRANSACTION',font=20)],
    [sg.Table(values=transactionList,headings=['PRODUCT NAME','AMOUNT','PRICE'],expand_x=True,key='--posTrans--')],
    [sg.Text(text='GST/HST:',font=20),sg.Text(text='',key='-hstText-',font=20),sg.Text(text='TOTAL:',font=20),sg.Text(text='',key='-totalTax-',font=20)],
    [sg.Button(button_text='LOG TRANSACTION',key='-posLog-'),sg.Button(button_text='CLEAR',key='-posClear-')]
    ]

employeeLayout = [
    [sg.Push(),sg.Text("EMPLOYEE INFORMATION SERVICE"),sg.Push()],
    [sg.Table(values=personList,headings=['FULL NAME','SALARY (MONTHLY)','PHONE NUMBER','ADDRESS'],expand_x=True,expand_y=True,key='--employeeList--')],
    [sg.Text(text='Employee Name',size=27),sg.Text(text='Salary',size=27),sg.Text(text='Phone #',size=27), sg.Text(text='Address',size=27)],
    [sg.Push(),sg.Text(text='EMPLOYEE ENTRY'),sg.Push()],
    [sg.Input(key='-empName-',size=27),sg.Input(key='-empSal-',size=27),sg.Input(key='-empPhon-'),sg.Input(key='-empAddr-')],
    [sg.Button(button_text='ENTER EMPLOYEE',key='-empAdd-')]
]

financialLayout = []

menu_def = []

mainLayout = [[sg.Menu(menu_def)],
             [sg.TabGroup([[sg.Tab("Home", homepageLayout,key='-homeTab-'), 
                            sg.Tab("Inventory", inventoryLayout,key='-invTab-'),
                            sg.Tab("Point of Sales",posLayout,key='-posTab-'),
                            sg.Tab("Employee Info",employeeLayout,key='-empTab-'),
                            sg.Tab("Financial Info",financialLayout,key='-finTab-')]],size=(720,720),enable_events=True)]] #<-- fits to window

mainPage = sg.Window("Universal Business Solutions",mainLayout,size=(720,720))

