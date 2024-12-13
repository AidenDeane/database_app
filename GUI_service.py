import PySimpleGUI as sg


passwordLayout = [
    [sg.Text('Please enter your password!')],
    [sg.Input(key='-pw-'), sg.Button('OK')] # key -pw- acts as identifier for events
    ]
passwordPage = sg.Window('Password',passwordLayout)

homepageLayout = [ 
    [sg.Push(), sg.Text("Welcome to the Universal Business Portal!",font=('Arial',20)), sg.Push()],
    [sg.Button('Inventory',key='-inv-',enable_events=True)]
     ]
#homepage = sg.Window('Home', homepageLayout, size=(720,720))

inventoryLayout = [
    [sg.Table([[1,2,3],[4,5,6],[7,8,9]],headings=['a','b','c'],expand_x=True)],
    [sg.Text("Database")]
]
#inventoryPage = sg.Window('Inventory',inventoryLayout, size=(720,720))

menu_def = []


mainLayout = [[sg.Menu(menu_def)],
             [sg.TabGroup([[sg.Tab("Home", homepageLayout), sg.Tab("Inventory", inventoryLayout)]],size=(720,720))]]

mainPage = sg.Window("Database",mainLayout,size=(720,720))

