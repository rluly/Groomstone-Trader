# Imports
from cmath import e
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
liabilities = []
equities = []
income_before_tax = []
income_tax_expense = []
operating_income = []
assets = []
operating_cashflow = []
capital_expendiatures = []

def clearLists():
    close.clear()
    volume.clear()
    ebitda_list.clear()
    cash.clear()
    longdebt.clear()
    shortdebt.clear()
    liabilities.clear()
    equities.clear()
    income_before_tax.clear()
    income_tax_expense.clear()
    operating_income.clear()
    assets.clear()
    operating_cashflow.clear()
    capital_expendiatures.clear()

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
        income_before_tax.append(i['incomeBeforeTax'])
        income_tax_expense.append(i['incomeTaxExpense'])
        operating_income.append(i['operatingExpenses'])

def parse_Balance(tick):
    path = './data/' + tick + '/' + tick + '_balance.json'
    f = open(path)
    data = json.load(f)
    for i in data['quarterlyReports']:
        cash.append(i['cashAndCashEquivalentsAtCarryingValue'])
        longdebt.append(i['currentLongTermDebt'])
        shortdebt.append(i['shortLongTermDebtTotal'])
        liabilities.append(i['totalLiabilities'])
        equities.append(i['totalShareholderEquity'])
        assets.append(i['totalAssets'])

def parse_Cash(tick):
    path = './data/' + tick + '/' + tick + '_cash.json'
    f = open(path)
    data = json.load(f)
    for i in data['quarterlyReports']:
        operating_cashflow.append(i['operatingCashflow'])
        capital_expendiatures.append(i['capitalExpenditures'])

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

def calc_DE():
    debt = 0
    equity = 0
    if(liabilities[0] != 'None'): debt = int(liabilities[0])
    if(equities[0] != 'None'): equity = int(equities[0])
    return debt/equity

def calc_ROIC():
    ibt = 0
    ite = 0
    oi = 0
    ic = 0
    nopat = 0
    if(income_before_tax[0] != 'None'): ibt = int(income_before_tax[0])
    if(income_tax_expense[0] != 'None'): ite = int(income_tax_expense[0])
    if(operating_income[0] != 'None'): oi = int(operating_income[0])
    if(assets != 'None'): ic = int(assets[0])
    nopat = oi*(1-(ite/ibt))
    return nopat/ic

def calc_FCFY():
    oc = 0
    ce = 0
    if(operating_cashflow[0] != 'None'): oc = int(operating_cashflow[0])
    if(capital_expendiatures[0] != 'None'): ce = int(capital_expendiatures[0])
    return oc-ce

def calc_WACC():
    E = round(float(close[0])) * int(volume[0])
    D = 0
    ibt = 0
    ite = 0
    Re = 0
    Rd = 0
    if(liabilities[0] != 'None'): D = int(liabilities[0])
    V = E + D
    if(income_before_tax[0] != 'None'): ibt = int(income_before_tax[0])
    if(income_tax_expense[0] != 'None'): ite = int(income_tax_expense[0])
    T = ite/ibt



def full_Parse(tick):
    parse_Daily(tick)
    parse_Income(tick)
    parse_Balance(tick)
    parse_Cash(tick)

def full_Analysis(tick):
    path = './data/' + tick + '/' + tick + '_calc.csv'
    with open(path, 'w') as f:
        res = str(calc_EVEBITDA(tick))
        print("The EVEBITDA for " + tick + " is " + res)
        f.write(res)
        f.write('\n')
        res = str(calc_DE())
        print("The D/E for " + tick + " is " + res)
        f.write(res)
        f.write('\n')
        res = str(calc_ROIC())
        print("THE ROIC for " + tick + " is " + res)
        f.write(res)
        f.write('\n')
        res = str(calc_FCFY())
        print("The FCFY for " + tick + " is " + res)
        f.write(res)
        f.write('\n')
    f.close()

f = open("tickers.txt","r")
for x in f:
    tickers.append(x.strip())

for tick in tickers:
    full_Parse(tick)
    full_Analysis(tick)
    clearLists()