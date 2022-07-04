import csv

symbol = []
industry = []

def hasE(tick):
    for x in tick:
        if x == 'E':
            return 1
    return 0

with open("stocks-list.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if hasE(row['Market Cap']) == 1:
            symbol.append(row['ï»¿Symbol'])
            industry.append(row['Industry'])
        elif(int(row['Market Cap']) > 1500000000): 
            symbol.append(row['ï»¿Symbol'])
            industry.append(row['Industry'])

with open('tickers.txt', 'a') as f:
    for x in symbol:
        f.write(x)
        f.write('\n')
f.close()

with open('industry.txt', 'a') as f:
    for x in industry:
        f.write(x)
        f.write('\n')
f.close()