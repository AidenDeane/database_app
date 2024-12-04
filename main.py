import PySimpleGUI as sg
import time
from GUI_service import *

passwordChallenge = False

## Password challenge
'''----------'''
while passwordChallenge == False:
    values, event = passwordPage.read()
    #print(values, event)
    if event == {'-pw-': 'pass'}: # if key -pw- has value of 'pass'
        print(event)
        passwordPage.close() # closes window
        passwordChallenge = True # Opens other window
'''----------'''

## Homepage
'''---------'''
while passwordChallenge == True:
    event = homepage.read() #Launches the window
    print(event)
    ## Open inventory window
    if event == ('-inv-', {}):
        homepage.hide()
        values, event = inventoryPage.read()
        if event == sg.WIN_CLOSED:
            print('asdasd')

    
