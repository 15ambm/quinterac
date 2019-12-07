'''
This file handles all forms of validation 
This includes validating account numbers, deposit, withdraw and transfer amounts
It also includes the updateDailyLimits() function, used to update the global dictionaries
in main that keep track of daily withdraw, transfer and deposit limits
'''
def updateDailyLimits():
    empty_limit_dict = {}
    file = open('./valid_account_list.txt','r')
    for line in file:
        try:
            account = int(line.rstrip())
            empty_limit_dict[account] = 0
        except:
            pass
    return empty_limit_dict

def validateAccountNumber(account_num):
    file = open('./valid_account_list.txt','r')
    for line in file:
        try:
            account = int(line.rstrip())
            if account_num == account:
                file.close()
                return True
        except:
            pass
    file.close()
    return False

def validateAccountNumberFormat(account_num):
    if len(str(account_num)) != 7 or int(str(account_num)[:1]) == 0 or type(account_num) == type(str):
        return False
    else:
        return True

def validateAccountNameFormat(account_name):
    length = len(account_name)
    if length > 30 or length < 3:
        return False
    else:
        return True

#need to add logic to check account_num in this function by calling others
def validateDepositAmount(account_num, amount, mode, daily_limits):
    if mode == 0 and (amount > 200000 or amount < 0):
            return False
    elif mode == 1 and (amount > 99999999 or amount < 0):
            return False
    else:
        try:
            daily_amount = daily_limits[account_num]
        except:
            return False
        if daily_amount + amount > 500000 and mode == 0:
            return False
        else:
            del daily_limits[account_num]
            daily_limits[account_num] = daily_amount + amount
            #will need logic to clean after every "day"
            return daily_limits

#need to add logic to check account_num in this function by calling others
def validateWithdrawAmount(account_num, amount, mode, daily_limits):
    #should it be a different daily_limits that is passed in?
    if mode == 0 and (amount > 100000 or amount < 0):
        return False
    elif mode == 1 and (amount > 99999999 or amount < 0):
        return False
    else:
        try:
            daily_amount = daily_limits[account_num]
#are these the right variables? they are used in old version of this function
        except:
            return False
        if daily_amount + amount > 500000:
            return False
        else:
            del daily_limits[account_num]
            daily_limits[account_num] = daily_amount + amount
            return daily_limits


def validateTransferAmount(amount, account_num, mode, daily_limits):
    if mode == 0 and (amount > 1000000 or amount < 0):
            return False
    elif mode == 1 and (amount > 99999999 or amount < 0):
            return False
    else:
        try:
            daily_amount = daily_limits[account_num]
        except:
            return False
        if daily_amount + amount > 1000000 and mode == 0:
            return False
        else:
            del daily_limits[account_num]
            daily_limits[account_num] = daily_amount + amount
            # will need logic to clean after every "day"
            return daily_limits