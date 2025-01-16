import datetime
import os 

hhmmTime = datetime.datetime.now().strftime("%H:%M")

transactionList = []
x=0
filename = (f'{datetime.date.today()}_transaction')
def save_transaction():
    filepath = os.path.join(f"{os.getcwd()}/transaction_logs/{filename}.txt") # Makes it so it can be dropped anywhere and still function. (I pray that I am right. Did not test this.)
    openFile = open(filepath, 'a') # Opens the filepath; appends information to file instead of overwriting like 'w' would. If file does not exist, it will be created automagically
    openFile.write(f"{hhmmTime} {transactionList}\n") # https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/
    openFile.close()