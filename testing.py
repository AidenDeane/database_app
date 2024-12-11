import PySimpleGUI as sg
from GUI_service import *

tablayout = [[sg.TabGroup([[sg.Tab("Tab 1", homepageLayout), sg.Tab("Tab 2", inventoryLayout)]])]]

mainwindow = sg.Window('Asdasfg',tablayout)

mainwindow.read()