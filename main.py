import PySimpleGUI as sg
import time
from GUI_service import *
from database_array import *
from pos_service import *

passwordChallenge = True # <-- Change to false upon release
totalNoHST = 0 #<-- for POS function

#TODO MAKE SHIT FLOAT!

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
        #newItem = Item(event['-prodName-'],event['-prodRP-'],event['-inInv-'],event['-prodID-']) # Turns gathered values into item class
        x = (event['-prodName-']+'Item') 
        x = Item(event['-prodName-'],int(event['-prodRP-']),int(event['-inInv-']),event['-prodID-']) # Turns gathered values into item class
        update_database()
        mainPage['--database--'].Update(dataList) # Updates the table with the item list
        print(dataList)
    elif values == '-posCheck-':
        for items in range(len(Item.data)):
            if event['-checkoutName-'] == Item.data[items].name or event['-checkoutName-'] == int(Item.data[items].item_id) :  # If inputted name = name in Item.data
                if int(event['-checkoutAmnt-']) <= Item.data[items].in_inventory and int(event['-checkoutAmnt-']) > 0:
                    Item.data[items].in_inventory -= int(event['-checkoutAmnt-']) # Subtract Item.data from inputted value
                    update_database() # Update dataList 
                    mainPage['--database--'].Update(dataList) # Update the display table "automagically" 
                    mainPage['-posName-'].Update("NAME OK!")
                    mainPage['-posInv-'].Update("AMOUNT OK!")

                    #'''POS TRANSACTION TABLE'''#
                    transactionList.append([Item.data[items].name,event['-checkoutAmnt-'],int(Item.data[items].retail_price)*int(event['-checkoutAmnt-'])])
                    mainPage['--posTrans--'].Update(transactionList)

                    #'''PRICE VALUES'''#
                    totalNoHST += int(Item.data[items].retail_price)*int(event['-checkoutAmnt-'])
                    mainPage['-totalTax-'].Update(round(totalNoHST*1.13,2))
                    mainPage['-hstText-'].Update(round(totalNoHST*0.13,2))
                    break # TODO fix str input crashes 
                else:
                    print("asd")
                    mainPage['-posInv-'].Update("ERROR: BAD AMOUNT!")
                    break
            elif event['-checkoutName-'] != Item.data[items].name:
                mainPage['-posName-'].Update("ERROR: BAD NAME!") # Name not OK
    elif values == '-posLog-':
        transactionList.append([f"pre-tax:{totalNoHST} | w/tax:{round(totalNoHST*1.13,2)}"])
        save_transaction()
    
    ## Open inventory window 
    
