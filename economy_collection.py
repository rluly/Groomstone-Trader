import os
import requests
import time

#set up your api key as an environment variable ALPHAVANTAGE_API_KEY
api_key = os.getenv('ALPHAVANTAGE_API_KEY')
base_url = 'https://www.alphavantage.co/query?'


def get_GDP():
    path = './economy/GDP.csv'
    params = {'function': 'REAL_GDP',
         'datatype': 'csv', 
		 'apikey': api_key}
    response = requests.get(base_url,params=params)
    with open(path,'wb') as file:
        file.write(response.content)

def get_GDP_Capita():
    path = './economy/GDP_Per_Capita.csv'
    params = {'function': 'REAL_GDP_PER_CAPITA',
         'datatype': 'csv', 
		 'apikey': api_key}
    response = requests.get(base_url,params=params)
    with open(path,'wb') as file:
        file.write(response.content)

def get_Treasury_Yield():
    path = './economy/Treasury_Yield.csv'
    params = {'function': 'TREASURY_YIELD',
         'datatype': 'csv', 
		 'apikey': api_key}
    response = requests.get(base_url,params=params)
    with open(path,'wb') as file:
        file.write(response.content)

def get_Federal_Funds_Rate():
    path = './economy/Federal_Funds_Rate.csv'
    params = {'function': 'FEDERAL_FUNDS_RATE',
         'datatype': 'csv', 
		 'apikey': api_key}
    response = requests.get(base_url,params=params)
    with open(path,'wb') as file:
        file.write(response.content)

def get_CPI():
    path = './economy/CPI.csv'
    params = {'function': 'CPI',
         'datatype': 'csv', 
		 'apikey': api_key}
    response = requests.get(base_url,params=params)
    with open(path,'wb') as file:
        file.write(response.content)

def get_Inflation():
    path = './economy/Inflation.csv'
    params = {'function': 'INFLATION',
         'datatype': 'csv', 
		 'apikey': api_key}
    response = requests.get(base_url,params=params)
    with open(path,'wb') as file:
        file.write(response.content)

def get_Inflation_Expectation():
    path = './economy/Inflation_Expectation.csv'
    params = {'function': 'INFLATION_EXPECTATION',
         'datatype': 'csv', 
		 'apikey': api_key}
    response = requests.get(base_url,params=params)
    with open(path,'wb') as file:
        file.write(response.content)

def get_Consumer_Sentiment():
    path = './economy/Consumer_Sentiment.csv'
    params = {'function': 'CONSUMER_SENTIMENT',
         'datatype': 'csv', 
		 'apikey': api_key}
    response = requests.get(base_url,params=params)
    with open(path,'wb') as file:
        file.write(response.content)

def get_Retail_Sales():
    path = './economy/Retail_Sales.csv'
    params = {'function': 'RETAIL_SALES',
         'datatype': 'csv', 
		 'apikey': api_key}
    response = requests.get(base_url,params=params)
    with open(path,'wb') as file:
        file.write(response.content)

def get_Durables():
    path = './economy/Durables.csv'
    params = {'function': 'DURABLES',
         'datatype': 'csv', 
		 'apikey': api_key}
    response = requests.get(base_url,params=params)
    with open(path,'wb') as file:
        file.write(response.content)

def get_Unemployment():
    path = './economy/Unemployment.csv'
    params = {'function': 'UNEMPLOYMENT',
         'datatype': 'csv', 
		 'apikey': api_key}
    response = requests.get(base_url,params=params)
    with open(path,'wb') as file:
        file.write(response.content)

def get_Nonfarm():
    path = './economy/Nonfarm.csv'
    params = {'function': 'NONFARM_PAYROLL',
         'datatype': 'csv', 
		 'apikey': api_key}
    response = requests.get(base_url,params=params)
    with open(path,'wb') as file:
        file.write(response.content)

get_GDP()
get_GDP_Capita()
get_Treasury_Yield()
get_Federal_Funds_Rate()
get_CPI()
get_Inflation()
get_Inflation_Expectation()
get_Consumer_Sentiment()
get_Retail_Sales()
get_Durables()
get_Unemployment()
get_Nonfarm()