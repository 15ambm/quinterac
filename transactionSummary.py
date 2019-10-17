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
        return self.transaction_code + ' ' + self.account_number_to + ' '+ self.amount + ' ' + self.account_number_from + ' ' + self.account_name  +"\n"

def writeTransactionSummaryFile(transactions_list):
    # Writes the list of transactions to the transaction summary file
    transaction_summary_file = open("transaction_summary.txt","a")
    for transaction in transactions_list:
        transaction_summary_file.write(transaction.create_transaction_line())
    transaction_summary_file.close()

#basic test 
#writeTransactionSummaryFile([Transaction("EOS", "0000000", "000", "0000000", "***")])