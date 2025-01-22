# Name: Aiden Deane
# Title: Universal Business Portal - main.py
# Date: Final Commit 22 Jan 2025
# Description: Imports all relevant files and runs them.
# Improper use of inputs will crash the program, and I could not find enough time to make the financial log PERMANENT


import PySimpleGUI as sg
from GUI_service import *
from database_array import *
from pos_service import *
from employee_service import *
from financial_service import *
from config.database_log import *
from config.employee_log import *

passwordChallenge = False # <-- Change to false upon release
totalNoHST = 0 #<-- for POS function
profits = 0
expenditures = 0

genPass = 'pass'
adminPass = 'admin' 
#TODO MAKE 
## Password challenge
'''----------'''
while passwordChallenge == False:
    values, event = passwordPage.read()
    if event == {'-pw-': genPass}: # if key -pw- has value of 'pass'
        passwordPage.close() # closes window
        passwordChallenge = True # Opens other window
        break
    elif event == sg.WIN_CLOSED or sg.Exit(): # If user tries to close the window
        passwordPage.close() # Actually close it this time (This is to prevent an error popup)
        break
    else:
        continue # So it doesn't crash if something else miraculously happpens



'''----------'''
## Homepage
'''---------'''
while passwordChallenge == True: #If password is true, start main program
    values, event = mainPage.read() #Launches the window
    #print(values,event)
    
    if event[1] == '-homeTab-':
        # Checks for admin auth
        if event['-adminPass-'] == adminPass:
            mainPage['-empTab-'].Update(visible= True)
            mainPage['-finTab-'].Update(visible= True)
        
    elif event[1] == '-invTab-':
        if values == '-invAdd-':
            # Turns gathered values into item class

            ## Reload the dsvar list 
            filepath = os.path.join(f"{os.getcwd()}/config/database_log.py")
            file = open(filepath, mode = 'r', encoding = 'utf-8-sig')
            dsVar = eval(file.readline().split("=")[1].strip())
            ## Solution from Mr. Stewart for reloading file values at runtime

            for items in range(len(dsVar)): # For items in the stored data
                print(items,len(dsVar)-1,items == len(dsVar))
                if event['-prodName-'] in dsVar[items]: # If event name is already written to dsVar
                    print('yes')
                    Item.data[items].retail_price = float(event['-prodRP-']) # v
                    Item.data[items].in_inventory = int(event['-inInv-'])    # Replace values
                    break
                elif items == len(dsVar)-1 and event['-prodName-'] not in dsVar[items]:
                    print('max', dsVar[items])
                    createItem = (event['-prodName-']+'Item') 
                    createItem = Item(event['-prodName-'],float(event['-prodRP-']),int(event['-inInv-']),event['-prodID-']) # Turns gathered values into item class
                    break
                else: # If not stored
                    continue # Continue until maximum reached
            update_database() # adds values into dataList
            mainPage['--database--'].Update(dataList) # Updates the table with the item list

    elif event[1] == '-posTab-':
        if values == '-posCheck-':
            for items in range(len(Item.data)):
                if event['-checkoutName-'] == Item.data[items].name or event['-checkoutName-'] == Item.data[items].item_id:  # If inputted name = name in Item.data
                    if int(event['-checkoutAmnt-']) <= Item.data[items].in_inventory and int(event['-checkoutAmnt-']) > 0:
                        Item.data[items].in_inventory -= int(event['-checkoutAmnt-']) # Subtract Item.data from inputted value
                        update_database() # Update dataList 
                        mainPage['--database--'].Update(dataList) # Update the display table "automagically" 
                        mainPage['-posName-'].Update("NAME OK!")
                        mainPage['-posInv-'].Update("AMOUNT OK!")

                        #'''POS TRANSACTION TABLE'''#
                        transactionList.append([Item.data[items].name,event['-checkoutAmnt-'],float(Item.data[items].retail_price)*int(event['-checkoutAmnt-'])])
                        mainPage['--posTrans--'].Update(transactionList)

                        #'''PRICE VALUES'''#
                        totalNoHST += float(Item.data[items].retail_price)*int(event['-checkoutAmnt-'])
                        mainPage['-totalTax-'].Update(round(totalNoHST*1.13,2))
                        mainPage['-hstText-'].Update(round(totalNoHST*0.13,2))
                        #'''FINANCIAL UPDATE'''#
                        break # TODO fix str input crashes 
                    else:
                        mainPage['-posInv-'].Update("ERROR: BAD AMOUNT!")
                        break
                elif event['-checkoutName-'] != Item.data[items].name:
                    mainPage['-posName-'].Update("ERROR: BAD NAME!") # Name not OK
        elif values == '-posLog-':
            if totalNoHST == 0: # Only check 1 since they go hand-in-hand
                continue
            else: # Log transaction
                transactionList.append([f"pre-tax:{totalNoHST} | w/tax:{round(totalNoHST*1.13,2)}"])
                profits += totalNoHST
                financialList.append(financial_update(profits,expenditures))
                mainPage['--financialTable--'].Update(financialList)
                save_transaction()
                ## Clear transaction after logging
                transactionList.clear()
                totalNoHST = 0
                mainPage['--posTrans--'].Update(transactionList)
                mainPage['-hstText-'].Update(totalNoHST)
                mainPage['-totalTax-'].Update(totalNoHST)
        elif values == '-posClear-': 
            # Clear point of sales from buttoin
            transactionList.clear()
            totalNoHST = 0
            mainPage['--posTrans--'].Update(transactionList)
            mainPage['-hstText-'].Update(totalNoHST)
            mainPage['-totalTax-'].Update(totalNoHST)
    elif event[1] == '-empTab-':
        # Add employee
        if values == '-empAdd-':

            filepath = os.path.join(f"{os.getcwd()}/config/employee_log.py")
            file = open(filepath, mode = 'r', encoding = 'utf-8-sig')
            empList = eval(file.readline().split("=")[1].strip())
            for people in range(len(Person.data)): # For items in the stored data
                if event['-empName-'] in empList[people]: # If event name is already written to dsVar
                    Person.data[people].salary = float(event['-empSal-'])
                    Person.data[people].phoneNo = int(event['-empPhon-']) # Replace values
                    Person.data[people].address = event['-empAddr-']
                    break
                elif people == len(empList)-1 and event['-empName-'] not in dsVar[people]:
                    createPerson = (event['-empName-']+'Person') 
                    createPerson = Person(event['-empName-'],float(event['-empSal-']),int(event['-empPhon-']),event['-empAddr-']) # Turns gathered values into item class
                    break
                else: # If not stored
                    continue
            update_people()
            mainPage['--employeeList--'].Update(personList)
    elif event[1] == '-finTab-':
        if values == '-finAdd-':
            financialList.append([str(event['-qVal-']),float(event['-proVal-']),float(event['-expVal-']),(float(event['-proVal-'])-float(event['-expVal-']))])
            mainPage['--financialTable--'].Update(financialList)
            for transactions in range(len(financialList)-1): # If name is in list
                if event['-qVal-'] in financialList[transactions]:
                    # Replace expend and profit
                    financialList[transactions][1] += float(event['-proVal-'])
                    financialList[transactions][2] += float(event['-expVal-'])
                    financialList[transactions][3] += float(event['-proVal-']) - float(event['-expVal-'])
                    # Remove dupe 
                    financialList.pop()
                    mainPage['--financialTable--'].Update(financialList)
                    break
                else: # create new 
                    continue
    elif event == sg.WIN_CLOSED or sg.Exit():
        mainPage.close()
        break
                    
    else:
        continue
    