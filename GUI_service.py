import PySimpleGUI as sg
import PySimpleGUI as sg

passwordLayout = [
    [sg.Text('Please enter your password!')],
    [sg.Input(key='-pw-'), sg.Button('OK')]
    ]
passwordPage = sg.Window('Password',passwordLayout)

homepageLayout = [ 
    [sg.Push(), sg.Text("Welcome to the Universal Business Portal!",font=('Arial',20)), sg.Push()],
    [sg.Button('Inventory',key='-inv-',enable_events=True)]
     ]
homepage = sg.Window('Home', homepageLayout, size=(720,720))

inventoryLayout = [
    [sg.Text('Testing')]
]
inventoryPage = sg.Window('Inv',inventoryLayout, size=(720,720))




