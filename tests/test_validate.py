import pytest
from app.validate import *
# validateAccountNumber Tests
def test_invalid_account_num():
    assert validateAccountNumber('AAA') == False

def test_valid_account_num():
    assert validateAccountNumber(9999999) == False

# validateAccountNumberFormat Tests
def test_valid_account_number_format():
    assert validateAccountNumberFormat('1234567') == True

def test_invalid_account_number_format():
    assert validateAccountNumberFormat('0234567') == False
    assert validateAccountNumberFormat('123') == False
    assert validateAccountNumberFormat('12345678') == False
# validateAccountNameFormat Tests
def test_valid_account_name_format():
    assert validateAccountNameFormat('Marc') == True

def test_invaild_account_name_format():
    # too short
    assert validateAccountNameFormat('a') == False
    # too long
    assert validateAccountNameFormat('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa') == False

    