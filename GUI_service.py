import PySimpleGUI as sg

passwordChallenge = False

## Password challenge
'''----------'''
while passwordChallenge == False:
    passwordLayout = [
        [sg.Text('Please enter your password!')],
        [sg.Input(key='-pw-'), sg.Button('OK')]
    ]
    passwordPage = sg.Window('Password',passwordLayout)
    values, event = passwordPage.read()
    print(values, event)
    if event == {'-pw-': 'pass'}: # if key -pw- has value of 'pass'
        passwordChallenge = True # closes the window
'''----------'''

## Homepage
'''---------'''
homepageLayout = [ 
    [sg.Text("Hello!",font=('Arial',20)  )  ]
     ]

homepage = sg.Window('Home', homepageLayout, size=(720,720))

if passwordChallenge == True:
    homepage.read() #Launches the window