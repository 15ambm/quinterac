'''
This file contains the definition of the Transaction object
It handles reading and writing from the transaction_summary.txt file
'''
class Transaction:
    # Use to keep track of the transactions made in the session
    def __init__(self, transaction_code, account_number_to, amount, account_number_from, account_name):
        self.transaction_code = transaction_code
        self.account_number_to = account_number_to
        self.amount = amount
        self.account_number_from = account_number_from
        self.account_name = account_name
    def create_transaction_line(self):
        # Returns the transaction information formatted for the transaction summary file
        return self.transaction_code + ' ' + str(self.account_number_to) + ' ' + str(self.amount) + ' ' + str(self.account_number_from) + ' ' + self.account_name  +"\n"

# Writes the list of transactions to the transaction summary file
def writeTransactionSummaryFile(transactions_list):
    transaction_summary_file = open("transaction_summary.txt","a")
    for transaction in transactions_list:
        transaction_summary_file.write(transaction.create_transaction_line())
    transaction_summary_file.close()

# converts a single line from the transaction_summary.txt file to a Transaction object
def stringToTransaction(transactionString):
    x = transactionString.split(' ', 4)
    transaction = Transaction(x[0], int(x[1]), int(x[2]), int(x[3]), x[4])
    return transaction

# converts the transaction_summary.txt file to a list of Transaction objects
def getTransactionsList():
    transaction_summary_file = open("transaction_summary.txt","r")
    transaction_list = []
    line = transaction_summary_file.readline()
    while line:
        # This if statment ensures that no none type objects are added to the the transaction list
        if len(line.strip()) >= 1:
            transaction_list.append(stringToTransaction(line.strip()))
        line = transaction_summary_file.readline()    
    return transaction_list