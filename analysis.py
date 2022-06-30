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

def clearLists():
    close.clear()
    volume.clear()
    ebitda_list.clear()
    cash.clear()
    longdebt.clear()
    shortdebt.clear()

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
    long = 0
    short = 0
    cash_res = 0
    if(longdebt[0] != 'None'): long = int(longdebt[0])
    if(shortdebt[0] != 'None'): short = int(shortdebt[0])
    if(cash[0] != 'None'): cash_res = int(cash[0])
    ev = cap + long + short - cash_res
    # print("The EV for " + tick + " is " + str(ev))
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
    res = str(calc_EVEBITDA(tick))
    print("The EVEBITDA for " + tick + " is " + res)

f = open("tickers.txt","r")
for x in f:
    tickers.append(x.strip())

for tick in tickers:
    full_Parse(tick)
    full_Analysis(tick)
    clearLists()