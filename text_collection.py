import csv

symbol = []
industry = []
names = []
banned = ['ALVO','BFRS','BRDG','BRFS','BSMX','ELV','LYG','PGY','YY']

def hasE(tick):
    for x in tick:
        if x == 'E':
            return 1
    return 0

def isBanned(tick):
    for x in banned:
        if x == tick:
            return 1
    return 0

def hasPeriod(tick):
    for x in tick:
        if x== '.':
            return 1
    return 0

with open("stocks-list.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if isBanned(row['ï»¿Symbol']) != 1:
            if hasPeriod(row['ï»¿Symbol']) != 1:
                if hasE(row['Market Cap']) == 1:
                    symbol.append(row['ï»¿Symbol'])
                    industry.append(row['Industry'])
                    names.append(row['Company Name'])
                elif int(row['Market Cap']) > 1500000000: 
                    symbol.append(row['ï»¿Symbol'])
                    industry.append(row['Industry'])
                    names.append(row['Company Name'])

with open('tickers.txt', 'w') as f:
    for x in symbol:
        f.write(x)
        f.write('\n')
f.close()

with open('industry.txt', 'w') as f:
    for x in industry:
        f.write(x)
        f.write('\n')
f.close()

with open('names.txt', 'w') as f:
    for x in names:
        f.write(x)
        f.write('\n')
f.close()