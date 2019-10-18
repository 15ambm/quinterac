

def validateAccountNumber(account_num):
    file = open('valid_account_list.txt','r')
    for line in file:
        account = int(line.rstrip())
        if account_num == account:
            file.close()
            return True
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

def validateDepositAmount(amount, account_num, mode, daily_limits):
    try:
        amount = int(amount)
    except:
        return False
    if amount is '':
        return False
    if mode is 0:
        if amount > 200000:
            return False
    elif mode is 1:
        if amount > 99999999:
            return False

    for account in daily_limits:
        if account == account_num:
            daily_amount = daily_limits[account]
            if daily_amount + amount > 500000 and mode == 0:
                return False
            else:
                del daily_limits[account]
                daily_limits[account] = daily_amount + amount
                return daily_limits
    
    daily_limits[account_num] = amount
    return daily_limits

def validateWithdrawAmount(amount, account_num, mode, daily_limits):
    try:
        amount = int(amount)
    except:
        return False
    if amount is '':
        return False
    if mode is 0:
        if amount > 100000:
            return False
    elif mode is 1:
        if amount > 99999999:
            return False

    for account in daily_limits:
        if account == account_num:
            daily_amount = daily_limits[account]
            if daily_amount + amount > 500000 and mode == 0:
                return False
            else:
                del daily_limits[account]
                daily_limits[account] = daily_amount + amount
                return daily_limits
    
    daily_limits[account_num] = amount
    return daily_limits


def validateTransferAmount(amount, account_num, mode, daily_limits):
    try:
        amount = int(amount)
    except:
        return False
    if amount is '':
        return False
    if mode is 0:
        if amount > 1000000:
            return False
    elif mode is 1:
        if amount > 99999999:
            return False

    for account in daily_limits:
        if account == account_num:
            daily_amount = daily_limits[account]
            if daily_amount + amount > 1000000 and mode == 0:
                return False
            else:
                del daily_limits[account]
                daily_limits[account] = daily_amount + amount
                return daily_limits
    
    daily_limits[account_num] = amount
    return daily_limits
