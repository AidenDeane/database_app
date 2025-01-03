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
    if values == '-invAdd-':
        mainPage['--database--'].Update(dataList) # Updates the table with the item list
        newItem = Item(event['-prodName-'],event['-prodRP-'],event['-inInv-'],event['-prodID-']) # Turns gathered values into item class
        update_database()
    elif values == '-posCheck-':
        for items in range(len(Item.data)):
            if event['-checkoutName-'] == Item.data[items].name:  # If inputted name = name in Item.data
                if int(event['-checkoutAmnt-']) > Item.data[items].in_inventory:
                    print("asd")
                    mainPage['-posInv-'].Update("ERROR: NOT ENOUGH IN STOCK")
                    break
                else:
                    Item.data[items].in_inventory -= int(event['-checkoutAmnt-']) # Subtract Item.data from inputted value
                    update_database() # Update dataList 
                    mainPage['--database--'].Update(dataList) # Update the display table "automagically" 
                    mainPage['-posName-'].Update("NAME OK!") # Name OK
                    mainPage['-posInv-'].Update("AMOUNT OK")
                    break
            elif event['-checkoutName-'] != Item.data[items].name:
                mainPage['-posName-'].Update("ERROR: BAD NAME!") # Name not OK
                
    
    ## Open inventory window 
    
