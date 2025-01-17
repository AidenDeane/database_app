import PySimpleGUI as sg
from GUI_service import *
from database_array import *
from pos_service import *
from employee_service import *
from financial_service import *

passwordChallenge = True # <-- Change to false upon release
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
    print(values, event)
    if event == {'-pw-': genPass}: # if key -pw- has value of 'pass'
        passwordPage.close() # closes window
        values = ''
        passwordChallenge = True # Opens other window
        break
    elif event == sg.WIN_CLOSED or sg.Exit():
        passwordPage.close()
        break
    else:
        continue



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
            createItem = (event['-prodName-']+'Item') 
            if isinstance(((event['-prodRP-']) or (event['-inInv-']) or event['-prodID-']), str):
                print('asd')
            else:
                createItem = Item(event['-prodName-'],float(event['-prodRP-']),int(event['-inInv-']),event['-prodID-']) # Turns gathered values into item class
            update_database()
            mainPage['--database--'].Update(dataList) # Updates the table with the item list
            print(dataList) 
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
                print(financialList)
                mainPage['--financialTable--'].Update(financialList)
                print(financialList)
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
            createPerson = (event['-empName-']+'Person') 
            createPerson = Person(event['-empName-'],int(event['-empSal-']),int(event['-empPhon-']),event['-empAddr-']) 
            update_people()
            mainPage['--employeeList--'].Update(personList)
    elif event[1] == '-finTab-':
        if values == '-finAdd-':
            print(len(financialList),financialList)
            financialList.append([str(event['-qVal-']),float(event['-proVal-']),float(event['-expVal-']),(float(event['-proVal-'])-float(event['-expVal-']))])
            mainPage['--financialTable--'].Update(financialList)
            for transactions in range(len(financialList)-1): # If name is in list
                print(transactions,'blah')
                if event['-qVal-'] in financialList[transactions]:
                    print('is')
                    # Replace expend and profit
                    financialList[transactions][1] += float(event['-proVal-'])
                    financialList[transactions][2] += float(event['-expVal-'])
                    financialList[transactions][3] += float(event['-proVal-']) - float(event['-expVal-'])
                    # Remove dupe 
                    financialList.pop()
                    mainPage['--financialTable--'].Update(financialList)
                    break
                else: # create new 
                    print("not")
    elif event == sg.WIN_CLOSED or sg.Exit():
        mainPage.close()
        break
    else:
        continue