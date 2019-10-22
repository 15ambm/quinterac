# Quinterac banking system

# Globals
import cmd
from app.transaction_summary import *
from app.account import *
from app.features import deposit, withdraw, transfer
logged_in = False
mode = 0
daily_deposits = {}
daily_withdrawals= {}
daily_transfers = {}
transaction_list = []
deleted_accounts_list = []

def controller(user_input):
    global daily_deposits, daily_withdrawals, daily_transfers
    if user_input == ("login" or "Login"):
        login()
    elif user_input == ("logout" or "Logout"):
        logout()
    elif user_input == ("createacct") and mode == 1:
        transaction = createAccount()
        if transaction != False:
            transaction_list.append(transaction)
            print("Account successfully create")
    elif user_input == ("deleteacct") and mode == 1:
        transaction, deleted_account_num = deleteAccount()
        if transaction != False:
            deleted_accounts_list.append(deleted_account_num)
            transaction_list.append(transaction)
            print("Account successfully deleted")
    elif user_input == ("deposit"):
        transaction, new_daily_deposits = deposit(mode, daily_deposits)
        if transaction != False:
            transaction_list.append(transaction)
            daily_deposits = new_daily_deposits
            print("Successful deposit")
    elif user_input == ("withdraw"):
        transaction, new_daily_withdrawals = withdraw(mode, daily_withdrawals)
        if transaction != False:
            transaction_list.append(transaction)
            daily_withdrawals = new_daily_withdrawals
            print("Successful withdrawal")
    elif user_input == ("transfer"):
        transaction, new_daily_transfers = transfer(mode, daily_transfers)
        if transaction != False:
            transaction_list.append(transaction)
            daily_transfers = new_daily_transfers
            print("Successful transfer")
    else: 
        print("That is not a recognized command")

def login():
    global logged_in
    if logged_in:
        print("You are already logged in")
        return
    login_arg = input("Session Type: ")
    valid_loggin = validateLogin(login_arg)
    if(valid_loggin):
        logged_in = True
        print("logged in successfully")
        return
    else:
        logged_in = False
        print("could not log in")
        return

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
    # write to transaction summary file
    global logged_in, transaction_list
    logged_in = False
    # Add EOS Transaction
    EOS = Transaction("EOS", "0000000", "000", "0000000", "***")
    transaction_list.append(EOS)
    # Write to transaction summary file
    writeTransactionSummaryFile(transaction_list)   
    print("Successfully logged out")

def loop():
    print("Welcome to Quinterac!")
    while(True):
        print(logged_in, mode)
        user_input = input("command: ")
        controller(user_input)
        



loop()