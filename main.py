import PySimpleGUI as sg
import time
from GUI_service import *
from database_array import *

passwordChallenge = True # <-- Change to false upon release


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
    values, event = mainPage.read() #Launches the window
    #print(values,event)
    if values == '-invUpd-':
        newItem = Item(event['-prodName-'],event['-prodRP-'],event['-inInv-'],event['-prodID-']) # Turns gathered values into item class
        add_item()
        mainPage['--database--'].Update(dataList) # Updates the table with the item list
    elif values == '-posCheck-':
        for items in range(len(Item.data)):
            if event['-checkoutName-'] == Item.data[items].name:
                Item.data[items].in_inventory -=1
                mainPage['--database--'].Update(dataList)
    ## Open inventory window 
    
