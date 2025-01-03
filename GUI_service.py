import PySimpleGUI as sg
from database_array import *


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
    [sg.Push(), sg.Text("DATABASE"), sg.Push()],
    [sg.Table(values=dataList,headings=['PRODUCT NAME','RETAIL PRICE','IN INVENTORY','ITEM ID'],expand_x=True,expand_y=True,key='--database--')],
    [sg.Push(),sg.Text('PRODUCT ENTRY'),sg.Push()],
    [sg.Text(text="Product Name",size=27),sg.Text(text='Retail Price',size=27),sg.Text(text='In Inventory',size=27),sg.Text(text='Product ID',size=27)],
    [sg.Input(key='-prodName-',size=27),sg.Input(key='-prodRP-',size=27),sg.Input(key='-inInv-',size=27),sg.Input(key='-prodID-',size=27)],
    [sg.Button("Update",key='-invUpd-')]
]
#inventoryPage = sg.Window('Inventory',inventoryLayout, size=(720,720))

posLayout = [
    [sg.Push(), sg.Text("POINT OF SALES MODULE"), sg.Push()],
    [sg.Input(key='-checkoutName-'),sg.Input(key='-checkoutAmnt-'),sg.Button(key='-posCheck-')]
    ]

menu_def = []

mainLayout = [[sg.Menu(menu_def)],
             [sg.TabGroup([[sg.Tab("Home", homepageLayout), 
                            sg.Tab("Inventory", inventoryLayout,key='-invButton-'),
                            sg.Tab("POS Module",posLayout)]],size=(720,720))]]

mainPage = sg.Window("Universal Business Solutions",mainLayout,size=(720,720))

