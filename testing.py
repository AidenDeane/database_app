from tkinter import *
from tkinter import ttk
from buttonCommands import *

class label_class:
    def __init__(self,contents,fontname,fontsize,posx,posy):
        self = Label()
        self.config(text=contents,font=(fontname,fontsize))
        self.place(x=posx,y=posy)

'''class button_class:
    def __init__(self,contents,fontname,fontsize,cmd):
        self.contents = self.config(text)
        '''
        
window = Tk()
window.geometry('480x480')

testtext = label_class('hi','Times New Roman','20','100','200')


window.mainloop()
