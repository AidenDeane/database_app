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
        passwordPage.close() # closes window
        values = ''
        passwordChallenge = True # Opens other window
        break
    elif event == sg.WIN_CLOSED or sg.Exit():
        passwordPage.close()
        break
'''----------'''

## Homepage
'''---------'''
while passwordChallenge == True: #If password is true, start main program
    event = homepage.read() #Launches the window
    print(event, values)
    ## Open inventory window
    if event == ('-inv-', {}):
        homepage.hide()
        event = inventoryPage.read()
        print(event,values)
        if event == ('-hpgBack-', {}):
            homepage.un_hide()
            inventoryPage.Close = True
    elif event == sg.WIN_CLOSED or sg.Exit():
        homepage.close()
        print("asdfgdds")
        break