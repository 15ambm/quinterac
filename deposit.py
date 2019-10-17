
from validate import validateAccountNumber, validateDepositAmount
from transaction_summary import Transaction

def deposit(mode, daily_limit):
    # transaction object
    account_num = input("Please enter an account number: ")
    if(not validateAccountNumber(account_num)): 
        print("Invalid account number")
        return False
    else:
        amount = input("Please enter an amount to deposit: ")
        if(not validateDepositAmount(amount, mode, daily_limit)):
            print("Invalid deposit amount")
            return False
        else:
            return Transaction("DEP", account_num, amount, "0000000", '***')
