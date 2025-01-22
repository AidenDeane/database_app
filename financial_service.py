# Name: Aiden Deane
# Title: Universal Business Portal - database_array.py
# Date: Final Commit 22 Jan 2025
# Description: dedicated file for the financial service. All data is stored temporarily during runitme and resets upon closing.

import datetime

financialList = []

def financial_update(x,y):
    return ([datetime.datetime.now().strftime('%y-%m'),x,y,x-y])

