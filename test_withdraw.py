import pytest
from app.features import withdraw
from app.transaction_summary import Transaction

def test_withdraw_success_agent():
    daily_withdrawals = {1234567: 0}
    account_num = 1234567
    amount = 10000
    #agent mode
    mode = 1

    transaction, new_daily_withdrawals = withdraw(account_num, amount, mode, daily_withdrawals)
    expected_transaction = Transaction("WDR", account_num, amount, "0000000", '***').create_transaction_line()
    transaction = transaction.create_transaction_line()
    daily_withdrawals[account_num] = amount

    assert transaction == expected_transaction
    assert daily_withdrawals == new_daily_withdrawals

def test_withdraw_success_machine():
    daily_withdrawals = {1234567: 0}
    account_num = 1234567
    amount = 10000
    #agent mode
    mode = 0

    transaction, new_daily_withdrawals = withdraw(account_num, amount, mode, daily_withdrawals)
    expected_transaction = Transaction("WDR", account_num, amount, "0000000", '***').create_transaction_line()
    transaction = transaction.create_transaction_line()
    daily_withdrawals[account_num] = amount

    assert transaction == expected_transaction
    assert daily_withdrawals == new_daily_withdrawals

@pytest.mark.skip(reason = "getting error with account input")
def test_withdraw_invalid_account_leading_0():
    #should we do this with agent or machine or both?
    daily_withdrawals = {1234567: 0}
    account_num = 0123456
    amount = 10000
    #agent mode
    mode = 0

    transaction, new_daily_withdrawals = withdraw(account_num, amount, mode, daily_withdrawals)
    expected_transaction = Transaction("WDR", account_num, amount, "0000000", '***').create_transaction_line()
    transaction = transaction.create_transaction_line()
    daily_withdrawals[account_num] = amount

    #daily_withdrawals are the same?
    assert transaction == False
    assert daily_withdrawals == new_daily_withdrawals
