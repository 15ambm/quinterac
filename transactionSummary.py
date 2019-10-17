class Transaction:
    def __init__(self, transaction_code, account_number_to, amount, account_number_from, account_name):
        self.transaction_code = transaction_code
        self.account_number_to = account_number_to
        self.amount = amount
        self.account_number_from = account_number_from
        self.account_name = account_name

def writeTransactionSummaryFile(transactions_list):
    transaction_summary_file = open("transaction_summary.txt","a")
    for transaction in transactions_list:
        transaction_line = transaction.transaction_code + ' ' + transaction.account_number_to + ' '+ transaction.amount + ' ' + transaction.account_number_from + ' ' + transaction.account_name  +"\n"
        transaction_summary_file.write(transaction_line)
    transaction_summary_file.close()
