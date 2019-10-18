
from validate import validateAccountNumber, validateDepositAmount, validateWithdrawAmount, validateTransferAmount
from transaction_summary import Transaction


def deposit(mode, deposits):
    # transaction object
    account_num = input("Please enter an account number: ")
    if(not validateAccountNumber(account_num)): 
        print("Invalid account number")
        return False, {}
    else:
        amount = input("Please enter an amount to deposit: ")
        deposits = validateDepositAmount(amount, int(account_num), mode, deposits)
        if(deposits == False ):
            print("Invalid deposit amount")
            return False, {}
        else:
            return Transaction("DEP", account_num, amount, "0000000", '***'), deposits


def withdraw(mode, withdrawals):
    # transaction object
    account_num = input("Please enter an account number: ")
    if(not validateAccountNumber(account_num)): 
        print("Invalid account number")
        return False, {}
    else:
        amount = input("Please enter an amount to withdraw: ")
        withdrawals = validateWithdrawAmount(amount, int(account_num), mode, withdrawals)
        if(withdrawals == False ):
            print("Invalid withdraw amount")
            return False, {}
        else:
            return Transaction("WDR", account_num, amount, "0000000", '***'), withdrawals


def transfer(mode, transfers):
    # transaction object
    account_num = input("Please enter an account number: ")
    if(not validateAccountNumber(account_num)): 
        print("Invalid account number")
        return False, {}
    else:
        amount = input("Please enter an amount to transfer: ")
        transfers = validateTransferAmount(amount, int(account_num), mode, transfers)
        if(transfers == False ):
            print("Invalid transfer amount")
            return False, {}
        else:
            return Transaction("XFR", account_num, amount, "0000000", '***'), transfers
