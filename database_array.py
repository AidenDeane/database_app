# Name: Aiden Deane
# Title: Universal Business Portal - database_array.py
# Date: Final Commit 22 Jan 2025
# Description: Writes and saves data to database_log.py, and acts as a staging area for all item classes.

import os
from config.database_log import *

# Reads data from dsVar and makes it usable for the rest of the program. Only called on launch
def load_data():
    for items in range(len(dsVar)):                                           # Goes through dsVar 
        Item(dsVar[items][0],dsVar[items][1],dsVar[items][2],dsVar[items][3]) # And then turns it into an item!

    ## Rebuilds the list from scratch. Only happens on launch 
    filepath = os.path.join(f"{os.getcwd()}/config/database_log.py")
    classLog = open(filepath,'a')
    classLog.truncate(0) # Clear to rebuild list
    classLog.write(f'dsVar = {dataList}') 
    classLog.close()

dataList = [] # Data stored here during runtime
def update_database():
    dataList.clear() # Must clear data as it reconstructs the list from scratch
    for items in range(len(Item.data)): # assigns all items a number
        dataList.append([]) # Create 2d list
        dataList[items].append(Item.data[items].name) 
        dataList[items].append(Item.data[items].retail_price) 
        dataList[items].append(Item.data[items].in_inventory) 
        dataList[items].append(Item.data[items].item_id)
    #            ^^^^^                   ^^^^^
    #   Output list index       input list index
    
        # Write it to file
        filepath = os.path.join(f"{os.getcwd()}/config/database_log.py")
        classLog = open(filepath,'a')
        classLog.truncate(0) # Clear to rebuild list
        classLog.write(f'dsVar = {dataList}') 
        classLog.close()



class Item:
    data = []
    def __init__(self,name,retail_price,in_inventory,item_id):
        self.name = name
        self.retail_price = retail_price
        self.in_inventory = in_inventory
        self.item_id = str(item_id)
        Item.data.append(self) # object list


load_data()

update_database()
