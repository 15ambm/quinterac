# __quinterac__
Welcome to the repository for Queen's Old Fashioned Interactive Banking System

Created by Alex Mason, Ted Munn, and Marc De Verteuil

### Running quinterac
* open command prompt or terminal
* navigate to the quinterac directory
* use the following command: `python __main__.py`

### Running the Backend

`python backend.py`

### Running Test Suite

`python -m pytest`

Note: The test_full_system.py tests have major side effects and these tests are skipped by deafult.

## Available Commands

### `login`
The login command will begin a session. It takes one argument, the session type. Options are `agent` for an administrator session and `machine` for a regular session.

### `logout`
The logout command will end the current session and record the transactions performed in the session. 

### `quit`
The quit command represents the end of the day. There can be multiple sessions in one day (i.e. multiple logins and logouts.) The quit command ends the program and updates the master accounts list as well as the list of valid accounts. 

### `deposit`
The deposit command will deposit money into an account. Deposit takes two arguments. The first argument is the account number to deposit to. The second argument is the amount to deposit, in cents. 

### `withdraw`
The withdraw command will withdraw money from an account. Withdraw takes two arguments. The first argument is the account number to withdraw from. The second argument is the amount to withdraw, in cents. 

### `transfer`
The transfer command will transfer money between two accounts. Transfer takes three arguments. The first argument is the account number to move money out of. The second argument is the amount to transfer, in cents. The third argument is the account to transfer the money to. 

