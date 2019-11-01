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
        account_num, amount = getFeatureInput('deposit')
        if (account_num and amount) != False:
            transaction, new_daily_deposits = deposit(account_num, amount, mode, daily_deposits)
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
        return False, False
    # Getting account numbers is the same for all features so we can validate in our getFeatureInput function
    if(not validateAccountNumber(account_num)): 
        print("Invalid account number")
        return False, False
    try:
        # amounts are validated according to their features, so here we only check that they are valid numbers
        amount = int(input("Please enter an amount to %s: " % feature))
    except:
        print("Invalid %s amount" % feature)
        return False, False
    if(feature == 'transfer'):
        try:
            account_num2 = int(input("Please enter account number to transfer to: "))
        except:
            print("Invalid account number")
            return False, False, False
        if(not validateAccountNumber(7654321)): 
            print("Invalid account number")
            return False, False
        else:
            return account_num, amount, account_num2
    return account_num, amount

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
    global daily_deposits, daily_withdrawals, daily_transfers
    daily_deposits = daily_withdrawals = daily_transfers = updateDailyLimits()
    while(True):
        print("logged in:", logged_in, mode)
        user_input = input("command: ")
        controller(user_input)
        



loop()