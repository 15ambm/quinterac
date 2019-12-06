from os import listdir
from os.path import isfile, join
from backend import updateBackend
# import transactions
transaction_filenames = [f for f in listdir("./transactions") if isfile(join("./transactions", f))]

with open('merged_transaction_summary.txt', 'w') as outfile:
    for fname in transaction_filenames:
        with open("./transactions/" + fname) as infile:
            outfile.write(infile.read())
            
updateBackend()

