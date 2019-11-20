'''
This file contains the definition of the MasterAccount object
It handles reading and writing from the master_accounts_list.txt file
'''
class MasterAccount:
    # Use to keep track of the transactions made in the session
    def __init__(self,account_number, balance, account_name):
        self.account_number = account_number
        self.balance = balance
        self.account_name = account_name
    def create_master_account_line(self):
        # Returns the transaction information formatted for the transaction summary file
        return str(self.account_number) + ' ' + str(self.balance) + ' ' + str(self.account_name) + "\n"

def writeMasterAccountsFile(master_account_list):
    # Writes the list of transactions to the transaction summary file
    master_account_file = open("master_accounts_list.txt","w")
    for key, account in master_account_list.items():
        master_account_file.write(account.create_master_account_line())
    master_account_file.close()

def stringToMasterAccount(master_account_string):
    x = master_account_string.split(' ', 2)
    account = MasterAccount(int(x[0]), int(x[1]), x[2])
    return account

# converts the transaction_summary.txt file to a list of Transaction objects
def getMasterAccountsList():
    master_accounts_file = open("master_accounts_list.txt","r")
    master_accounts_list = {}
    line = master_accounts_file.readline()
    while line:
        # This if statment ensures that no none-type objects are added to the the transaction list
        if len(line.strip()) >= 1:
            account = stringToMasterAccount(line.strip())
            master_accounts_list[account.account_number] = account
        line = master_accounts_file.readline()    
    return master_accounts_list