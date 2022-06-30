#set up your api key as an environment variable ALPHAVANTAGE_API_KEY

# from alpha_vantage.timeseries import TimeSeries
# from alpha_vantage.foreignexchange import ForeignExchange
# from alpha_vantage.cryptocurrencies import CryptoCurrencies
# from alpha_vantage.techindicators import TechIndicators
# from alpha_vantage.sectorperformance import SectorPerformances
import os
import requests
import pandas as pd

# app = TimeSeries()
# aapl = app.get_daily(symbol='AAPL',outputsize='compact')
# print(aapl)

api_key = os.getenv('ALPHAVANTAGE_API_KEY')

#EBITA (as is)
base_url = 'https://www.alphavantage.co/query?'
params = {'function': 'INCOME_STATEMENT',
		 'symbol': 'IBM', 
		 'apikey': api_key}

response = requests.get(base_url,params=params)
with open('./data/IBM_income.json','wb') as file:
    file.write(response.content)

#EV (long debt, short debt, and cash)
base_url = 'https://www.alphavantage.co/query?'
params = {'function': 'BALANCE_SHEET',
		 'symbol': 'IBM', 
		 'apikey': api_key}

response = requests.get(base_url,params=params)
with open('./data/IBM_balance.json','wb') as file:
    file.write(response.content)

# df = pd.read_csv('./data/IBM.csv')
# df.set_index('timestamp',inplace=True)