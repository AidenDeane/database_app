import PySimpleGUI as sg

testdata = []
def add_item():
    testdata.clear()
    for items in range(len(Item.data)): # assigns all items a number
        testdata.append([]) # Create 2d list
        testdata[items].append(Item.data[items].name) 
        testdata[items].append(Item.data[items].retail_price) 
        testdata[items].append(Item.data[items].wholesale_price) 
        testdata[items].append(Item.data[items].item_id)
    #            ^^^^^                   ^^^^^
    #   Output list index       input list index

class Item:
    data = []
    def __init__(self,name,retail_price,wholesale_price,item_id):
        self.name = name
        self.retail_price = retail_price
        self.wholesale_price = wholesale_price
        self.item_id = item_id
        Item.data.append(self)

pencilItem = Item("pencil",20,40,65000)
testItem = Item("asd",1,2,3030)

dataUpd = [
    ['a','b','c','d']
    ]

## Gathers pre-programmed items into a list
'''---------'''


    
add_item()