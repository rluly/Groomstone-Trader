#Placeholder
import csv
import json

close = []
volume = []
cap = 0
ev = 0
ebitda_list = []
cash = []
longdebt = []
shortdebt = []

with open('./data/IBM_daily.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        close.append(row['close'])
        volume.append(row['volume'])

cap = round(float(close[0])) * int(volume[0])
# print(cap)


f = open('./data/IBM_income.json')
data = json.load(f)

for i in data['quarterlyReports']:
    ebitda_list.append(i['ebitda'])


f = open('./data/IBM_balance.json')
data = json.load(f)

for i in data['quarterlyReports']:
    cash.append(i['cashAndCashEquivalentsAtCarryingValue'])
    longdebt.append(i['currentLongTermDebt'])
    shortdebt.append(i['shortLongTermDebtTotal'])

ev = cap + int(longdebt[0]) + int(shortdebt[0]) - int(cash[0])
ebitda = int(ebitda_list[0])
print(ev/ebitda)