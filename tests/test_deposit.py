import pytest
from app.features import deposit
from app.transaction_summary import Transaction


def test_deposit_success_agent():
    daily_deposits = {1234567: 0}
    account_num = 1234567
    amount = 10000
    # Agent mode
    mode = 1
    
    # Call our deposit function
    transaction, new_daily_deposits = deposit(account_num, amount, mode, daily_deposits)
    # Create an expected Transaction
    expected_transaction = Transaction("DEP", account_num, amount, "0000000", '***').create_transaction_line()
    # We will compare the strings
    transaction = transaction.create_transaction_line()
    # update our initial daily_deposits dict to be our expected dict
    daily_deposits[account_num] = amount

    assert transaction == expected_transaction
    assert daily_deposits == new_daily_deposits

def test_deposit_success_machine():
    daily_deposits = {1234567: 0}
    account_num = 1234567
    amount = 10000
    # Machine mode
    mode = 0
    
    # Call our deposit function
    transaction, new_daily_deposits = deposit(account_num, amount, mode, daily_deposits)
    # Create an expected Transaction
    expected_transaction = Transaction("DEP", account_num, amount, "0000000", '***').create_transaction_line()
    # We will compare the strings
    transaction = transaction.create_transaction_line()
    # update our initial daily_deposits dict to be our expected dict
    daily_deposits[account_num] = amount

    assert transaction == expected_transaction
    assert daily_deposits == new_daily_deposits

'''
# Account numbers are checked before deposit is called so this is out of scope for the deposit feature
def test_deposit_invalid_account_number():
    daily_deposits = {}
    account_num = 1234567
    amount = 10000
    # Machine mode
    mode = 0
    
    # Call our deposit function
    transaction, new_daily_deposits = deposit(account_num, amount, mode, daily_deposits)
    # Create an expected Transaction
    expected_transaction = Transaction("DEP", account_num, amount, "0000000", '***').create_transaction_line()
    # We will compare the strings
    transaction = transaction.create_transaction_line()
    # update our initial daily_deposits dict to be our expected dict
    daily_deposits[account_num] = amount

    assert transaction == expected_transaction
    assert daily_deposits == new_daily_deposits
'''

def test_deposit_negative_amount_machine():
    daily_deposits = {1234567: 0}
    account_num = 1234567
    amount = -1
    # Machine mode
    mode = 0
    
    # Call our deposit function
    transaction, new_daily_deposits = deposit(account_num, amount, mode, daily_deposits)

    assert transaction == False
    assert new_daily_deposits == daily_deposits

def test_deposit_amount_too_large_machine():
    daily_deposits = {1234567: 0}
    account_num = 1234567
    amount = 200001
    # Machine mode
    mode = 0
    
    # Call our deposit function
    transaction, new_daily_deposits = deposit(account_num, amount, mode, daily_deposits)

    assert transaction == False
    assert new_daily_deposits == daily_deposits

def test_deposit_no_account_machine():
    daily_deposits = {}
    account_num = 1234567
    amount = 10000
    # Machine mode
    mode = 0
    
    # Call our deposit function
    transaction, new_daily_deposits = deposit(account_num, amount, mode, daily_deposits)

    assert transaction == False
    assert new_daily_deposits == daily_deposits

def test_deposit_over_daily_limit_machine():
    daily_deposits = {1234567: 490000}
    account_num = 1234567
    amount = 100000
    # Machine mode
    mode = 0
    
    # Call our deposit function
    transaction, new_daily_deposits = deposit(account_num, amount, mode, daily_deposits)

    assert transaction == False
    assert new_daily_deposits == daily_deposits

def test_deposit_negative_amount_agent():
    daily_deposits = {1234567: 0}
    account_num = 1234567
    amount = -1
    # Agent mode
    mode = 1
    
    # Call our deposit function
    transaction, new_daily_deposits = deposit(account_num, amount, mode, daily_deposits)

    assert transaction == False
    assert new_daily_deposits == daily_deposits

def test_deposit_amount_too_large_agent():
    daily_deposits = {1234567: 0}
    account_num = 1234567
    amount = 100000000
    # Agent mode
    mode = 1
    
    # Call our deposit function
    transaction, new_daily_deposits = deposit(account_num, amount, mode, daily_deposits)

    assert transaction == False
    assert new_daily_deposits == daily_deposits

def test_deposit_no_account_agent():
    daily_deposits = {}
    account_num = 1234567
    amount = 10000
    # Agent mode
    mode = 1
    
    # Call our deposit function
    transaction, new_daily_deposits = deposit(account_num, amount, mode, daily_deposits)

    assert transaction == False
    assert new_daily_deposits == daily_deposits


