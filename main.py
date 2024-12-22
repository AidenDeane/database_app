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
    print(testdata)
    values, event = mainPage.read() #Launches the window
    print(values,event)
    '''if values == '-invUpd-':
        print('adwfsgrefwqfrdbegrfwrf')
        Item.data.append(f'{dataUpd[0][0]}{dataUpd[0][1]}')
        mainPage.refresh()
        mainPage['--database--'].Update(testdata)
        print(testdata)'''
    ## Open inventory window 
    