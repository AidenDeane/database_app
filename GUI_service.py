import PySimpleGUI as sg


passwordLayout = [
    [sg.Text('Please enter your password!')],
    [sg.Input(key='-pw-'), sg.Button('OK')] # key -pw- acts as identifier for events
    ]
passwordPage = sg.Window('Password',passwordLayout)

homepageLayout = [ 
    [sg.Push(), sg.Text("Welcome to the Universal Business Portal!",font=('Arial',20)), sg.Push()]
     ]
#homepage = sg.Window('Home', homepageLayout, size=(720,720))

inventoryLayout = [
    [sg.Push(), sg.Text("DATABASE"), sg.Push()],
    [sg.Table([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],headings=['PRODUCT NAME','RETAIL PRICE','WHOLESALE PRICE','ITEM ID'],expand_x=True)],
    [sg.Push(),sg.Text('PRODUCT ENTRY'),sg.Push()],
    [sg.Table([[[],[],[],[]]],headings=['PRODUCT NAME','RETAIL PRICE','WHOLESALE PRICE','ITEM ID'],expand_x=True,enable_cell_editing=True,enable_events=True],
    [sg.Button("Update",enable_events=True,key='-invUpd-')]
]
#inventoryPage = sg.Window('Inventory',inventoryLayout, size=(720,720))

posLayout = []

menu_def = []

mainLayout = [[sg.Menu(menu_def)],
             [sg.TabGroup([[sg.Tab("Home", homepageLayout), 
                            sg.Tab("Inventory", inventoryLayout),
                            sg.Tab("POS Module",posLayout)]],size=(720,720))]]

mainPage = sg.Window("Universal Business Solutions",mainLayout,size=(720,720))

