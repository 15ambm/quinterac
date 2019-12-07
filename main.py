# Quinterac banking system
import cmd
import sys
from app.transaction_summary import *
from app.account import *
from app.features import deposit, withdraw, transfer

# Globals
logged_in = False
mode = 0
daily_deposits = {}
daily_withdrawals= {}
daily_transfers = {}
transaction_list = []
deleted_accounts_list = []

def main():
    loop()

def controller(user_input):
    global daily_deposits, daily_withdrawals, daily_transfers, logged_in

    if user_input == ("quit"):
        if logged_in == False:
            sys.exit()
        else:
            print("Please logout first")
    elif user_input == ("login" or "Login"):
        logged_in = login()
    elif logged_in == False:
        print("You are not logged in")
    elif user_input == ("logout" or "Logout"):
        logout()
        transaction_list.clear()        
    elif user_input == ("createacct") and mode == 1:
        account_num, account_name = getAccountInput()
        if (account_num  and account_num) != False:
            transaction = createAccount(account_num, account_name)
            transaction_list.append(transaction)
            print("Account successfully create")
    elif user_input == ("deleteacct") and mode == 1:
        transaction, deleted_account_num = deleteAccount()
        if transaction != False:
            deleted_accounts_list.append(deleted_account_num)
            transaction_list.append(transaction)
            print("Account successfully deleted")
    elif user_input == ("deposit"):
        account_num, amount = getFeatureInput('deposit')
        if (account_num and amount) != False:
            transaction, new_daily_deposits = deposit(account_num, amount, mode, daily_deposits)
            if transaction != False:
                transaction_list.append(transaction)
                daily_deposits = new_daily_deposits
                print("Successful deposit")
    elif user_input == ("withdraw"):
        account_num, amount = getFeatureInput('withdraw')
        if (account_num and amount) != False:
            transaction, new_daily_withdrawals = withdraw(account_num, amount, mode, daily_deposits)
            if transaction != False:
                transaction_list.append(transaction)
                daily_withdrawals = new_daily_withdrawals
                print("Successful withdrawal")
    elif user_input == ("transfer"):
        account_num, amount, account_num2 = getFeatureInput('transfer')
        if (account_num and amount and account_num2) != False:
            transaction, new_daily_transfers = transfer(mode, account_num, account_num2, amount, daily_transfers)
            daily_transfers = new_daily_transfers
            if transaction != False:
                transaction_list.append(transaction)
                print("Successful transfer")
    else: 
        print("That is not a recognized command")

def getFeatureInput(feature):
    try:
        account_num = int(input("Please enter an account number: "))
    except:
        print("Invalid account number")
        if feature == 'transfer':
            return False, False, False
        return False, False
    # Getting account numbers is the same for all features so we can validate in our getFeatureInput function
    if(not validateAccountNumber(account_num)):
        print("Invalid account number")
        if feature == 'transfer':
            return False, False, False
        else:
            return False, False
    try:
        # amounts are validated according to their features, so here we only check that they are valid numbers
        amount = int(input("Please enter an amount to %s: " % feature))
    except:
        print("Invalid %s amount" % feature)
        if feature == 'transfer':
            return False, False, False
        return False, False
    if(feature == 'transfer'):
        try:
            account_num2 = int(input("Please enter account number to transfer to: "))
        except:
            print("Invalid account number")
            return False, False, False
        if(not validateAccountNumber(account_num2)):
            print("Invalid account number")
            return False, False, False
        else:
            return account_num, amount, account_num2
    return account_num, amount

def getAccountInput():
    try:
        account_num = int(input("Please enter an account number: "))
    except:
        print("Invalid account number")
        return False, False
    if(not validateAccountNumberFormat(account_num)):
        print("Invalid account number")
        return False, False
    account_name = input("Please enter an account name: ")
    if(not validateAccountNameFormat(account_name)):
        print("Invalid account name")
        return False, False
    return account_num, account_name

def login():
    if logged_in:
        print("You are already logged in")
        return True
    login_arg = input("Session Type: ")
    valid_loggin = validateLogin(login_arg)
    if(valid_loggin):
        print("Logged in successfully")
        return True
    else:
        print("Could not log in")
        return False

def validateLogin(input):
    global mode
    if input == 'Machine' or input == 'machine':
        mode = 0
        return True
    elif input == 'Agent' or input == 'agent':
        mode = 1
        return True
    else:
        print("That is not an option")
        return False

def logout():
    global logged_in, transaction_list
    if logged_in == False:
        print("You are not logged in")
        return
    # write to transaction summary file
    logged_in = False
    # Add EOS Transaction
    EOS = Transaction("EOS", "0000000", "000", "0000000", "***")
    transaction_list.append(EOS)
    # Write to transaction summary file
    writeTransactionSummaryFile(transaction_list)
    print("Successfully logged out")

def loop():
    print("Welcome to Quinterac!")
    global daily_deposits, daily_withdrawals, daily_transfers
    daily_deposits = daily_withdrawals = daily_transfers = updateDailyLimits()
    while(True):
        user_input = input("> ")
        controller(user_input)
