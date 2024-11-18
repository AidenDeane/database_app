from tkinter import *
from tkinter import ttk
from buttonCommands import *

#Main window
mainWindow = Tk()
mainWindow.geometry('720x480')
mainWindow.title('Database Application')

#Title text
titleText = Label(mainWindow)
titleText.config(text='Welcome to The Database Software',font=('Helvetica',20))
titleText.place(x=10,y=20)

#menu bar
'''initialization'''
menubar = Menu(mainWindow)
mainWindow.config(menu=menubar)

menu1 = Menu(menubar)
menubar.add_cascade(label='Options',menu=menu1)
menu1.add_command(label='GitHub',command=github_link)
menu1.add_separator()
menu1.add_command(label='Quit',command=end)

# window menus
menu2 = Menu(menubar)
menubar.add_cascade(label='Menus',menu=menu2)

''''Inventory'''
menu2.add_command(label='Inventory')

inventory_window = Toplevel(mainWindow)

inventoryButton = Button(mainWindow)
inventoryButton.config(text="Inventory",width=5,height=2)
inventoryButton.pack()

#must be last else NOTHING works
mainWindow.mainloop()