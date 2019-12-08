from os import listdir
from os.path import isfile, join
# import transactions
onlyfiles = [f for f in listdir("./transactions") if isfile(join("./transactions", f))]
print(onlyfiles)
onlyfiles = onlyfiles[::-1]
print(onlyfiles)

with open('merged_.txt', 'w') as outfile:
    for fname in onlyfiles:
        with open("./transactions/" + fname) as infile:
            outfile.write(infile.read())
