# Imports
from cmath import e
import csv
import json

# Global Vars
tickers = []
industries = []
names = []
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
beta = 0.0
tenyear = 0.0
Rm = 0.0
PB = 0.0
PEG = 0.0
PE = 0.0
bookvalue = 0.0

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
    beta = 0.0
    tenyear = 0.0
    Rm = 0.0
    PB = 0.0
    PEG = 0.0
    PE = 0.0
    bookvalue = 0.0

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

def parse_Treasury():
    path = './economy/Treasury_Yield.csv'
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            tenyear = float(row['value'])
            break

def parse_Overview(tick):
    path = './data/' + tick + '/' + tick + '_overview.json'
    f = open(path)
    data = json.load(f)
    if(data['Beta'] != 'None'): beta = data['Beta']
    if(data['PriceToBookRatio'] != 'None'): PB = data['PriceToBookRatio']
    if(data['PERatio'] != 'None'): PE = data['PERatio']
    if(data['PEGRatio'] != 'None'): PEG = data['PEGRatio']
    if(data['BookValue'] != 'None'): bookvalue = data['BookValue']

def parse_VTI():
    path = './data/VTI/VTI_daily.csv'
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        x = 0
        start = 0
        finish = 0
        for row in reader:
            if(x == 0): finish = float(row['high'])
            elif(x == 255): start = float(row['high'])
            x = x + 1
    rm = finish/start

def calc_EV():
    cap = round(float(close[0])) * int(volume[0])
    long = 0
    short = 0
    cash_res = 0
    if(longdebt[0] != 'None'): long = int(longdebt[0])
    if(shortdebt[0] != 'None'): short = int(shortdebt[0])
    if(cash[0] != 'None'): cash_res = int(cash[0])
    ev = cap + long + short - cash_res
    return ev

def calc_EBITDA():
    ebitda = 0
    if(ebitda_list[0] != 'None'): ebitda = int(ebitda_list[0])
    return ebitda

def calc_EVEBITDA():
    if(calc_EBITDA() != 0): return calc_EV()/calc_EBITDA()
    else: return 17.12

def calc_DE():
    debt = 0
    equity = 0
    if(liabilities[0] != 'None'): debt = int(liabilities[0])
    if(equities[0] != 'None'): equity = int(equities[0])
    if(equity != 0): return debt/equity
    else: return 0

def calc_ROIC():
    ibt = 0
    ite = 0
    oi = 0
    ic = 0
    nopat = 0
    if(income_before_tax[0] != 'None'): ibt = int(income_before_tax[0])
    if(income_tax_expense[0] != 'None'): ite = int(income_tax_expense[0])
    if(operating_income[0] != 'None'): oi = int(operating_income[0])
    if(assets[0] != 'None'): ic = int(assets[0])
    if(ibt != 0): nopat = oi*(1-(ite/ibt))
    if(ic != 0): return nopat/ic
    else: return 0

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
    Rd = 0.04
    T = 0
    if(liabilities[0] != 'None'): D = int(liabilities[0])
    V = E + D
    if(income_before_tax[0] != 'None'): ibt = int(income_before_tax[0])
    if(income_tax_expense[0] != 'None'): ite = int(income_tax_expense[0])
    if(ibt != 0): T = ite/ibt
    Re = tenyear + beta * (Rm - T)
    if(V != 0): return (((E/V) * Re) + ((D/V * Rd) * (1-T)))
    else: return 0

def calc_ROICWACC():
    return calc_ROIC() - calc_WACC()

def full_Parse(tick):
    parse_Daily(tick)
    parse_Income(tick)
    parse_Balance(tick)
    parse_Cash(tick)
    parse_Overview(tick)

def full_Analysis(tick):
    path = './data/' + tick + '/' + tick + '_calc.csv'
    name = names[tickers.index(tick)]
    industry = industries[tickers.index(tick)]
    EVEBITDA = str(calc_EVEBITDA())
    DE = str(calc_DE())
    ROICWACC = str(calc_ROICWACC())
    FCFY = str(calc_FCFY())
    with open(path, 'w', newline = '') as f:
        fieldnames = ['Tick','Name','Industry','EV/EBITDA','D/E','ROIC-WACC','FCFY','P/E','P/B','Book Value','PEG','Beta']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'Tick': tick,
        'Name': name,
        'Industry': industry,
        'EV/EBITDA': EVEBITDA,
        'D/E': DE,
        'ROIC-WACC': ROICWACC,
        'FCFY': FCFY,
        'P/E': PE,
        'P/B': PB,
        'Book Value': bookvalue,
        'PEG': PEG,
        'Beta': beta})
    f.close()

parse_Treasury()
parse_VTI()

f = open("tickers.txt","r")
for x in f:
    tickers.append(x.strip())
f.close()

f = open("industry.txt","r")
for x in f:
    industries.append(x.strip())
f.close()

f = open("names.txt","r")
for x in f:
    names.append(x.strip())
f.close()

for tick in tickers:
    full_Parse(tick)
    print(tick + " is finished parsing.")
    full_Analysis(tick)
    print(tick + " is finished analyzing.")
    clearLists()