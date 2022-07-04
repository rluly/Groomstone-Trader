import os

tickers = []

f = open("tickers.txt","r")
for x in f:
    tickers.append(x.strip())

parent_dir = './data/'

for x in tickers:
    path = os.path.join(parent_dir,x)
    os.mkdir(path)
    print("Directory '%s s' created" % x)