import PySimpleGUI as sg

dataList = []
def add_item():
    dataList.clear()
    for items in range(len(Item.data)): # assigns all items a number
        dataList.append([]) # Create 2d list
        dataList[items].append(Item.data[items].name) 
        dataList[items].append(Item.data[items].retail_price) 
        dataList[items].append(Item.data[items].in_inventory) 
        dataList[items].append(Item.data[items].item_id)
    #            ^^^^^                   ^^^^^
    #   Output list index       input list index

class Item:
    data = []
    def __init__(self,name,retail_price,in_inventory,item_id):
        self.name = name
        self.retail_price = retail_price
        self.in_inventory = in_inventory
        self.item_id = item_id
        Item.data.append(self)

pencilItem = Item("pencil",20,40,65000)
testItem = Item("asd",1,2,3030)

## Gathers pre-programmed items into a list
'''---------'''


    
add_item()

'''for items in range(len(Item.data)):
    if event['-checkoutName-']+'Item' == Item.data[items].name:
        print('match')'''