

def validateAccountNumber(account_num):
    file = open('valid_account_list.txt','r')
    for line in file:
        account = int(line.rstrip())
        if account_num == account:
            file.close()
            return False
    if len(account_num) != 7 or int(str(account_num)[:1]) == 0 or type(account_num) == type(str):
        return False
    else:
        return True

def validateAccountName(account_name):
    length = len(account_name)
    if length > 30 and length < 3:
        return False
    else:
        return True

def validateDepositAmount(amount, mode, daily_limit):
    if amount is '':
        return False
    if mode is 0:
        if int(amount) > 200000:
            return False
        elif (daily_limit + int(amount)) > 500000:
            return False
        else:
            return True
    elif mode is 1:
        if int(amount) > 9999999999:
            return False
        else:
            return True
    else:
        return True