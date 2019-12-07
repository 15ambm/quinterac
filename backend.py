'''
This file handles the backend processing at the end of a day
It updates the master_accounts_list and valid_account_list text files
based on the days transactions 
'''

from app.transaction_summary import *
from app.master_account import *
import os

def backendController(transaction, master_accounts_list):

    if transaction.transaction_code == "DEP":
        return deposit(transaction, master_accounts_list)
    if transaction.transaction_code == "WDR":
        return withdraw(transaction, master_accounts_list)
    if transaction.transaction_code == "XFR":
        return transfer(transaction, master_accounts_list)
    if transaction.transaction_code == "NEW":
        return createAccount(transaction, master_accounts_list)
    if transaction.transaction_code == "DEL":
        return deleteAccount(transaction, master_accounts_list)

    return master_accounts_list


def deposit(transaction, master_accounts_list):
    #preforms a deposit operation given an account number and an amount
    #check that deposit does not push account over max value
    current_account_balance = master_accounts_list[transaction.account_number_to].balance
    #print(type(master_accounts_list[transaction.account_number_to].balance))
    if(current_account_balance + transaction.amount < 99999999):
        master_accounts_list[transaction.account_number_to].balance = current_account_balance + transaction.amount
    return master_accounts_list

def withdraw(transaction, master_accounts_list):
    #preforms a withdraw operation given an account number and an amount
    #check that account has enough funds to compelete the withdraw
    current_account_balance = master_accounts_list[transaction.account_number_to].balance
    if(current_account_balance - transaction.amount >= 0):
        master_accounts_list[transaction.account_number_to].balance = current_account_balance - transaction.amount
    return master_accounts_list

def transfer(transaction, master_accounts_list):
    #preforms a transfer operation given a to and from account number and an amount
    #Do deposit check on the to account and the withdraw check on the from account 
    from_account_balance = master_accounts_list[transaction.account_number_from].balance
    to_account_balance = master_accounts_list[transaction.account_number_to].balance
    if(from_account_balance - transaction.amount >= 0): 
        if(to_account_balance + transaction.amount < 99999999):
            master_accounts_list[transaction.account_number_to].balance = to_account_balance + transaction.amount
            master_accounts_list[transaction.account_number_from].balance = from_account_balance - transaction.amount
    return master_accounts_list

def createAccount(transaction, master_accounts_list):
    #preforms a create account operation given an account number and account name
    master_accounts_list[transaction.account_number_to] = MasterAccount(transaction.account_number_to, 0, transaction.account_name)
    return master_accounts_list

def deleteAccount(transaction, master_accounts_list):
    #preforms a delete account operation given an account number and account name
    #insure account has 0 balance and account_num and name_match
    account = master_accounts_list[transaction.account_number_to]
    if(account.balance == 0):
            del master_accounts_list[transaction.account_number_to]
    return master_accounts_list

def generateValidAccountsList(master_accounts_list):
    # Writes the list of accounts from the master accounts list to the valid_accounts_list
    valid_accounts_list = open("valid_account_list.txt","w")
    for key, account in master_accounts_list.items():
        valid_accounts_list.write(str(key) + '\n')
    valid_accounts_list.write('\n')
    valid_accounts_list.close()

def mergeTransactions():
    transaction_filenames = [f for f in os.listdir("./transactions") if os.path.isfile(os.path.join("./transactions", f))]
    with open('merged_transaction_summary.txt', 'w') as outfile:
        for fname in transaction_filenames:
            with open("./transactions/" + fname) as infile:
                outfile.write(infile.read())

def clearTransactions():
    transaction_filenames = [f for f in os.listdir("./transactions") if os.path.isfile(os.path.join("./transactions", f))]
    for file in transaction_filenames:
        os.remove("./transactions/{}".format(file))

def updateBackend():
    mergeTransactions()
    transaction_list = getTransactionsList()
    master_accounts_list = getMasterAccountsList()
    for transaction in transaction_list:
        master_accounts_list = backendController(transaction, master_accounts_list)
    writeMasterAccountsFile(master_accounts_list)
    generateValidAccountsList(master_accounts_list)
    clearTransactions()

updateBackend()
