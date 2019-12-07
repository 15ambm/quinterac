import tempfile
from importlib import reload
import os
import io
import sys
import main as app
import pytest
from backend import updateBackend

path = os.path.dirname(os.path.abspath(__file__))

''' 
-------------------------------------------------------------------------------------------
WARNING
THE TEST FUNCTIONS IN THIS FILE HAVE MAJOR SIDEEFFECTS AND WILL CHANGE THE MASTER ACCOUNTS LIST
AND THE VALID ACCOUNTS LIST, TO RUN THEM PLEASE COMMENT OUT THE SKIP DECORATOR  
-------------------------------------------------------------------------------------------
''' 

# The daily tests tuns one session (i.e. login -> stuff -> logout)
# It will NOT affect master_accounts_list.txt, valid_account_list.txt, merged_transaction_summary.txt 
# however it WILL change the /transaction directory by adding a new set of transactions
@pytest.mark.skip(reason="Side Effects")
def test_daily(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
'''login
agent
deposit
1234567
1000
withdraw
7654321
1000
createacct
1029384
Coolaccount
logout
'''])

# The weekly test runs multiple sessions on multiple days.
# Each day is separated by an invocation of updateBackend(), which updates
# master_accounts_list.txt, valid_account_list.txt, merged_transaction_summary.txt and the entire /transactions directory
@pytest.mark.skip(reason="Side Effects")
def test_weekly(capsys):
    
    day_one = "login\nagent\ncreateacct\n1234567\nAlex\ncreateacct\n7773332\nTed\ncreateacct\n4567891\nMarc\nlogout\nquit"
    day_two = "login\nmachine\ndeposit\n1234567\n1000\nlogout\nlogin\nmachine\ndeposit\n7773332\n25000\ndeposit\n4567891\n60000\nlogout\nquit"
    day_three = "login\nmachine\ntransfer\n7773332\n5000\n1234567\nwithdraw\n7773332\n2500\nlogout\nlogin\nmachine\nwithdraw\n4567891\n60000\nlogout\nquit"
    day_four = "login\nagent\ncreateacct\n9871234\nSavings\ndeleteacct\n4567891\nMarc\nlogout\nquit"
    day_five = "login\nmachine\ndeposit\n9871234\n8000\nlogout\nlogin\nmachine\ntransfer\n1234567\n2000\n9871234\nlogout\nquit"

    try:
        helper( capsys=capsys, terminal_input=[day_one])
    except:
        pass
    updateBackend()
    try:
        helper( capsys=capsys, terminal_input=[day_two])
    except:
        pass
    updateBackend()
    try:
        helper( capsys=capsys, terminal_input=[day_three])
    except:
        pass
    updateBackend()
    try:
        helper( capsys=capsys, terminal_input=[day_four])
    except:
        pass
    updateBackend()
    try:
        helper( capsys=capsys, terminal_input=[day_five])
    except:
        pass
    updateBackend()
    
# The helper function runs our quinterac program and stubs the terminal input with pre-chosen values
def helper(capsys, terminal_input):
    reload(app)
    sys.argv = ['main.py']
    sys.stdin = io.StringIO(
        os.linesep.join(terminal_input))
    app.main()
    