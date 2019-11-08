
from app.transaction_summary import *
from app.master_account import *

def backendController(transaction):

    if transaction.transaction_code == "DEP":
        pass
    if transaction.transaction_code == "WDR":
        pass
    if transaction.transaction_code == "XFR":
        pass
    if transaction.transaction_code == "NEW":
        pass
    if transaction.transaction_code == "DEL":
        pass

def updateBackend():
    transaction_list = getTransactionsList()
    master_accounts_list = getMasterAccountsList()
    for transaction in transaction_list:
        backendController(transaction)
        pass
