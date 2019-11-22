import pytest
from app.backend import *
from app.master_account import MasterAccount
from app.transaction_summary import Transaction

def test_withdraw_valid_amount():
    master_accounts_list = {}
    master_accounts_list[1234567] = MasterAccount(1234567, 1000, 'testaccount')
    transaction = Transaction('WDR',1234567, 100, 0000000 , '***')
    backendController(transaction, master_accounts_list)
    assert master_accounts_list[1234567].balance == 900
    
def test_withdraw_invalid_amount():
    master_accounts_list = {}
    master_accounts_list[1234567] = MasterAccount(1234567, 1000, 'testaccount')
    transaction = Transaction('WDR',1234567, 10000, 0000000, '***')
    backendController(transaction, master_accounts_list)
    assert master_accounts_list[1234567].balance == 1000