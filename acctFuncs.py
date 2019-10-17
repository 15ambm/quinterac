


# format of accounts is AAAA MMMM NNNN accountNumber amount name
def create_acct(acctNum):
    try:
        strAcctNum = str(acctNum)
    except:
        print('Invalid Account Number')
        return 0

    acctNumLength = len(strAcctNum)

    if acctNumLength != 7:
        print('Invalid Account Number')
        return 0


    else:
        accountInfo = strAcctNum
        file = open(fileName,"r")
        for line in file:
            if accountInfo == str(line):
                return 0

        file = open(fileName,"a")
        file.write(accountInfo + "\n")
        # print(accountInfo)
        return 1
# print(create_acct(1111114))

# A function that prints all of the accounts in the acct list file
def print_accounts_list():
    fileName = 'acctList.txt'
    file = open(fileName,"r")

    for line in file:
        thisLine = line.rstrip()
        print(thisLine)
    file.close()

#a function that takes in an account number and checks if its in the acct list
def check_in_list(accountNumberIn):
    fileName = 'acctList.txt'
    file = open(fileName,"r")
    for line in file:
        thisLine = line.rstrip()
        thisLine = int(thisLine)
        if accountNumberIn == thisLine:
            return 1
    return 0
    file.close()

print_accounts_list()
print(check_in_list(1234567))
