import PySimpleGUI as sg
import time
passwordChallenge = False


## Password challenge
'''----------'''
while passwordChallenge == False:
    passwordLayout = [
        [sg.Text('Please enter your password!')],
        [sg.Input(key='-pw-'), sg.Button('OK')]
        ]
    passwordPage = sg.Window('Password',passwordLayout)
    values, event = passwordPage.read()
    #print(values, event)
    if event == {'-pw-': 'pass'}: # if key -pw- has value of 'pass'
        passwordChallenge = True # closes the window
'''----------'''

## Homepage
'''---------'''

homepageLayout = [ 
    [sg.Push(), sg.Text("Welcome to the Universal Business Portal!",font=('Arial',20)), sg.Push()],
    [sg.Button('Inventory',enable_events=True)]
     ]

inventoryLayout = [
    [sg.Text('Testing')]
]

homepage = sg.Window('Home', homepageLayout, size=(720,720))
inventoryPage = sg.Window('Inv',inventoryLayout,)

while passwordChallenge == True:
    event,values = homepage.read() #Launches the window
    
