import pytest
from main import validateLogin, login
import unittest.mock
from app.transaction_summary import Transaction
from app.account import createAccount


def test_validate_login_success_machine():
    login_mode = "machine"
    assert validateLogin(login_mode) == True
        
    login_mode = "Machine"
    assert validateLogin(login_mode) == True

def test_validate_login_success_agent():
    login_mode = "agent"
    assert validateLogin(login_mode) == True

    login_mode = "Agent"
    assert validateLogin(login_mode) == True

def test_validate_login_failure():
    login_mode = ""
    assert validateLogin(login_mode) == False

def test_login_success():
    with unittest.mock.patch('builtins.input', return_value="machine"):
        assert login() == True
    with unittest.mock.patch('builtins.input', return_value="agent"):
        assert login() == True
    with unittest.mock.patch('builtins.input', return_value="Machine"):
        assert login() == True
    with unittest.mock.patch('builtins.input', return_value="Agent"):
        assert login() == True

def test_create_account_success():
    account_num = 1234567
    account_name = "Alex"

    expected_transaction = Transaction("NEW", account_num, "000", "0000000", account_name).create_transaction_line()
    transaction = createAccount(account_num, account_name).create_transaction_line()

    assert transaction == expected_transaction


