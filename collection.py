import os
import requests
# import pandas as pd

#set up your api key as an environment variable ALPHAVANTAGE_API_KEY
api_key = os.getenv('ALPHAVANTAGE_API_KEY')
base_url = 'https://www.alphavantage.co/query?'
tickers = []
f = open("tickers.txt","r")
for x in f:
    tickers.append(x.strip())

def get_Daily(tick):
    path = './data/' + tick + '/' + tick + '_daily.csv'
    params = {'function': 'TIME_SERIES_DAILY',
		 'symbol': tick, 
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

for tick in tickers:
    get_Daily(tick)
    get_Income(tick)
    get_Balance(tick)