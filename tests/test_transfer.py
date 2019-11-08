import pytest
from app.features import transfer
from app.transaction_summary import Transaction

def test_transfer_success_agent():
    daily_transfer = {1234567: 0}
    account_num_from = 1234567
    account_num_to = 1122334
    amount = 10
    # Agent mode
    mode = 1
    
    # Call our deposit function
    transaction, new_daily_transfers = transfer(mode, account_num_from, account_num_to, amount, daily_transfer)
    # Create an expected Transaction
    expected_transaction = Transaction("XFR", account_num_to, amount, account_num_from, '***').create_transaction_line()
    # We will compare the strings
    transaction = transaction.create_transaction_line()
    # update our initial daily_deposits dict to be our expected dict
    daily_transfer[account_num_from] = amount

    assert transaction == expected_transaction
    assert daily_transfer == new_daily_transfers
def test_transfer_success_atm():
    daily_transfer = {1234567: 0}
    account_num_from = 1234567
    account_num_to = 1122334
    amount = 10
    # Agent mode
    mode = 0
    
    # Call our deposit function
    transaction, new_daily_transfers = transfer(mode, account_num_from, account_num_to, amount, daily_transfer)
    # Create an expected Transaction
    expected_transaction = Transaction("XFR", account_num_to, amount, account_num_from, '***').create_transaction_line()
    # We will compare the strings
    transaction = transaction.create_transaction_line()
    # update our initial daily_deposits dict to be our expected dict
    daily_transfer[account_num_from] = amount

    assert transaction == expected_transaction
    assert daily_transfer == new_daily_transfers
'''
# Account numbers are checked before transfer is called so this is out of scope for the deposit feature
def test_transfer_to_invalid_account():
    daily_transfer = {1234567: 0}
    account_num_from = 1234567
    account_num_to = 7654321
    amount = 10
    # Agent mode
    mode = 1
    
    # Call our deposit function
    transaction, new_daily_transfers = transfer(mode, account_num_from, account_num_to, amount, daily_transfer)

    # We will compare the strings
    transaction = transaction.create_transaction_line()
    # update our initial daily_deposits dict to be our expected dict
    daily_transfer[account_num_from] = amount

    assert transaction == False
    assert daily_transfer == new_daily_transfers
'''
def test_transfer_invalid_amount_atm():
    daily_transfer = {1234567: 0}
    account_num_from = 1234567
    account_num_to = 7654321
    amount = 1000001
    # ATM mode
    mode = 0
    
    # Call our deposit function
    transaction, new_daily_transfers = transfer(mode, account_num_from, account_num_to, amount, daily_transfer)

    # update our initial daily_deposits dict to be our expected dict

    assert transaction == False
    assert new_daily_transfers == daily_transfer

def test_transfer_invalid_amount_agent():
    daily_transfer = {1234567: 0}
    account_num_from = 1234567
    account_num_to = 7654321
    amount = 100000000
    # ATM mode
    mode = 1
    
    # Call our deposit function
    transaction, new_daily_transfers = transfer(mode, account_num_from, account_num_to, amount, daily_transfer)

    # update our initial daily_deposits dict to be our expected dict

    assert transaction == False
    assert new_daily_transfers == daily_transfer 

def test_transfer_invalid_total_amount_atm():
    daily_transfer = {1234567: 1000000}
    account_num_from = 1234567
    account_num_to = 7654321
    amount = 1
    # ATM mode
    mode = 0
    
    # Call our deposit function
    transaction, new_daily_transfers = transfer(mode, account_num_from, account_num_to, amount, daily_transfer)

    # update our initial daily_deposits dict to be our expected dict

    assert transaction == False
    assert new_daily_transfers == daily_transfer 
