'''
This file handles the primary features of the banking system, including
deposits, withdrawals, and transfers
'''
from app.validate import validateAccountNumber, validateDepositAmount, validateWithdrawAmount, validateTransferAmount
from app.transaction_summary import Transaction

def deposit(account_num, amount, mode, deposits):
    new_daily_deposits = validateDepositAmount(account_num, amount, mode, deposits)
    if(new_daily_deposits == False ):
        print("Invalid deposit amount")
        return False, deposits
    else:
        return Transaction("DEP", account_num, amount, "0000000", '***'), deposits


def withdraw(account_num, amount, mode, withdrawals):
    # updated this function to match deposit above
    new_daily_withdrawals = validateWithdrawAmount(account_num, amount, mode, withdrawals)
    if (new_daily_withdrawals == False):
        print("Invalid withdrawal amount")
        return False, withdrawals
    else:
        return Transaction("WDR", account_num, amount, "0000000", '***'), withdrawals

    '''
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
'''

def transfer(mode, account_num1, account_num2, amount, transfers):
    # transaction object
    new_daily_transfers = validateTransferAmount(amount, int(account_num1), mode, transfers)
    if(new_daily_transfers == False ):
        print("Invalid transfer amount")
        return False, transfers
    else:
        return Transaction("XFR", account_num2, amount, account_num1, '***'), transfers
