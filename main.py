
# Quinterac banking system

# Globals
import cmd
from transactionSummary import *
logged_in = False
mode = 0
transaction_list =[]
deleted_accounts_list =[]

def controller(user_input):
    if user_input == ("login" or "Login"):
        login()
    elif user_input == ("logout" or "Logout"):
        logout()
    elif user_input == ("createacct") and mode == 1:
        createAccount()
    elif user_input == ("deleteacct") and mode == 1:
        deleteAccount()
    else: 
        print("That is not a recognized command")
    

def login():
    global logged_in
    login_arg = input("Session Type: ")
    if logged_in:
        print("You are already logged in")
        return
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
    global logged_in
    logged_in = False
    # Add EOS Transaction
    EOS = Transaction("EOS", "0000000", "000", "0000000", "***")
    transaction_list.append(EOS)
    # Write to transaction summary file
    writeTransactionSummaryFile(transaction_list)
    print("Successfully logged out")

def createAccount():
    # transaction object
    if mode != 1:
        print("You do not have create account privilege")
        return

    account_num = input("Please enter an account number: ")
    if(not validateAccountNumber(account_num)): 
        print("Invalid account number")
        return
    else:
        account_name = input("Please enter an account name: ")
        if(not validateAccountName(account_name)):
            print("Invalid account name")
        else:
            # create new transaction and add to transaction list
            create_account_transaction = Transaction("NEW", account_num, "000", "0000000", account_name)
            transaction_list.append(create_account_transaction)

def deleteAccount():
    if mode != 1:
        print("You do not have delete account privilege")
        return
    account_num = input("Please enter an account number: ")
    if(not validateAccountNumber(account_num)): 
        print("Invalid account number")
        return
    else:
        account_name = input("Please enter an account name: ")
        if(not validateAccountName(account_name)):
            print("Invalid account name")
        else:
            # create new transaction and add to transaction list
            deleted_accounts_list.append(account_num)
            create_account_transaction = Transaction("DEL", account_num, "000", "0000000", account_name)
            transaction_list.append(create_account_transaction)

def validateAccountNumber(account_num):
    if len(account_num) != 7 and int(str(account_num)[:1]) != 0:
        return False
    else:
        return True

def validateAccountName(account_name):
    length = len(account_name)
    if length > 30 and length < 3:
        return False
    else:
        return True

def loop():
    print("Welcome to Quinterac!")
    while(True):
        print(logged_in, mode)
        user_input = input("command: ")
        controller(user_input)
        



loop()