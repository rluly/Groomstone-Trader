# Imports
import csv
import json

# Global Vars
tickers = []
close = []
volume = []
ebitda_list = []
cash = []
longdebt = []
shortdebt = []

def parse_Daily(tick):
    path = './data/' + tick + '/' + tick + '_daily.csv'
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            close.append(row['close'])
            volume.append(row['volume'])

def parse_Income(tick):
    path = './data/' + tick + '/' + tick + '_income.json'
    f = open(path)
    data = json.load(f)
    for i in data['quarterlyReports']:
        ebitda_list.append(i['ebitda'])

def parse_Balance(tick):
    path = './data/' + tick + '/' + tick + '_balance.json'
    f = open(path)
    data = json.load(f)
    for i in data['quarterlyReports']:
        cash.append(i['cashAndCashEquivalentsAtCarryingValue'])
        longdebt.append(i['currentLongTermDebt'])
        shortdebt.append(i['shortLongTermDebtTotal'])

def calc_EV(tick):
    cap = round(float(close[0])) * int(volume[0])
    ev = cap + int(longdebt[0]) + int(shortdebt[0]) - int(cash[0])
    return ev

def calc_EBITDA(tick):
    ebitda = int(ebitda_list[0])
    return ebitda

def calc_EVEBITDA(tick):
    return calc_EV(tick)/calc_EBITDA(tick)

def full_Parse(tick):
    parse_Daily(tick)
    parse_Income(tick)
    parse_Balance(tick)

def full_Analysis(tick):
    print(calc_EVEBITDA(tick))

f = open("tickers.txt","r")
for x in f:
    tickers.append(x.strip())

for tick in tickers:
    full_Parse(tick)
    full_Analysis(tick)