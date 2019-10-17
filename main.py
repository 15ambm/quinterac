# Quinterac banking system

# Globals
import cmd
from transaction_summary import *
from account import *
from deposit import deposit
logged_in = False
mode = 0
daily_deposit_limit = 0
transaction_list = []
deleted_accounts_list = []

def controller(user_input):
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
        transaction = deposit(mode, daily_deposit_limit)
        if transaction != False:
            transaction_list.append(transaction)
            print("Successful deposit")
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