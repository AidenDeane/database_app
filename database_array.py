import os
from config.database_log import *


def load_data():
    for items in range(len(dsVar)):
        print(dsVar[items][0],dsVar[items][1],dsVar[items][2],dsVar[items][3])
        Item(dsVar[items][0],dsVar[items][1],dsVar[items][2],dsVar[items][3])

dataList = []
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
        Item.data.append(self)



load_data()

update_database()
