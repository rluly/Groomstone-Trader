import os
import requests
import time

#set up your api key as an environment variable ALPHAVANTAGE_API_KEY
api_key = os.getenv('ALPHAVANTAGE_API_KEY')
base_url = 'https://www.alphavantage.co/query?'
tickers = []
f = open("tickers.txt","r")
for x in f:
    tickers.append(x.strip())

def get_Daily(tick):
    path = './data/' + tick + '/' + tick + '_daily.csv'
    params = {'function': 'TIME_SERIES_DAILY_ADJUSTED',
		 'symbol': tick,
         'outputsize' : 'compact', 
         'datatype': 'csv',
		 'apikey': api_key}
    response = requests.get(base_url,params=params)
    with open(path,'wb') as file:
        file.write(response.content)

def get_Income(tick):
    path = './data/' + tick + '/' + tick + '_income.json'
    params = {'function': 'INCOME_STATEMENT',
		 'symbol': tick, 
		 'apikey': api_key}
    response = requests.get(base_url,params=params)
    with open(path,'wb') as file:
        file.write(response.content)

def get_Balance(tick):
    path = './data/' + tick + '/' + tick + '_balance.json'
    params = {'function': 'BALANCE_SHEET',
		 'symbol': tick, 
		 'apikey': api_key}
    response = requests.get(base_url,params=params)
    with open(path,'wb') as file:
        file.write(response.content)

def get_Cash(tick):
    path = './data/' + tick + '/' + tick + '_cash.json'
    params = {'function': 'CASH_FLOW',
		 'symbol': tick, 
		 'apikey': api_key}
    response = requests.get(base_url,params=params)
    with open(path,'wb') as file:
        file.write(response.content)

def get_Earnings(tick):
    path = './data/' + tick + '/' + tick + '_earnings.json'
    params = {'function': 'Earnings',
		 'symbol': tick, 
		 'apikey': api_key}
    response = requests.get(base_url,params=params)
    with open(path,'wb') as file:
        file.write(response.content)

def get_Overview(tick):
    path = './data/' + tick + '/' + tick + '_overview.json'
    params = {'function': 'OVERVIEW',
		 'symbol': tick, 
		 'apikey': api_key}
    response = requests.get(base_url,params=params)
    with open(path,'wb') as file:
        file.write(response.content)

for tick in tickers:
    get_Daily(tick)
    get_Income(tick)
    get_Balance(tick)
    get_Cash(tick)
    get_Earnings(tick)
    get_Overview(tick)
    print(tick + " has finished collecting.")
    time.sleep(1) #Necessary for 75 calls/minute restriction