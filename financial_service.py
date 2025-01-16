import datetime

financialList = []

finDate = datetime.datetime.now().strftime('%y-%m')
profits = 0
expend = 0


def financial_update(x,y):
    return ([datetime.datetime.now().strftime('%y-%m'),x,y,x-y])

print('asd')