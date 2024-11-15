from tkinter import *
from buttonCommands import *
#import webbrowser


'''def githublink(): # 
    url = 'https://github.com/AidenDeane'
    webbrowser.open(url,new=3)

def end():
    quit()'''

#Main window
mainWindow = Tk()
mainWindow.geometry('480x480')
mainWindow.title('Database Application')

#Title text
titleText = Label(mainWindow)
titleText.config(text='Welcome to The Database Software',font=('Helvetica',20))
titleText.pack()

#menu Bar
menubar = Menu(mainWindow)

mainWindow.config(menu=menubar)

fileMenu = Menu(menubar)
menubar.add_cascade(label='Options',menu=fileMenu)
fileMenu.add_command(label='GitHub',command=github_link)
fileMenu.add_separator()
fileMenu.add_command(label='Quit',command=end)

#inventory button

inventoryButton = Button(mainWindow)
inventoryButton.config(text="asd",width=5,height=2)
inventoryButton.place(x=10,y=40)

#must be last
mainWindow.mainloop()

#test THIS DOESNT WORK
