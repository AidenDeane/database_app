import PySimpleGUI as sg

menu_def = [['&Github', ['!&hbk',]]]

layout = [[sg.Menu(menu_def)],
          [sg.Text('Your window!', size=(30, 5))]]


page = sg.Window('test',layout)
page.read()