from app.transaction_summary import *
from app.validate import *

def createAccount():
    # transaction object
    account_num = input("Please enter an account number: ")
    if(not validateAccountNumberFormat(account_num)): 
        print("Invalid account number")
        return False
    else:
        account_name = input("Please enter an account name: ")
        if(not validateAccountNameFormat(account_name)):
            print("Invalid account name")
            return False
        else:
            # create new transaction and add to transaction list
            print(type(account_num))
            return Transaction("NEW", account_num, "000", "0000000", account_name)

def deleteAccount():
    account_num = input("Please enter an account number: ")
    if(not validateAccountNumberFormat(account_num)): 
        print("Invalid account number")
        return False
    else:
        account_name = input("Please enter an account name: ")
        if(not validateAccountNameFormat(account_name)):
            print("Invalid account name")
            return False
        else:
            # create new transaction and add to transaction list
            return Transaction("DEL", account_num, "000", "0000000", account_name), account_num
