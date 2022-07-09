import os
import requests

#set up your api key as an environment variable ALPHAVANTAGE_API_KEY
api_key = os.getenv('ALPHAVANTAGE_API_KEY')
base_url = 'https://www.alphavantage.co/query?'

path = './data/VTI/VTI_daily.csv'
params = {'function': 'TIME_SERIES_DAILY_ADJUSTED',
		 'symbol': 'VTI',
         'outputsize' : 'full', 
         'datatype': 'csv',
		 'apikey': api_key}
response = requests.get(base_url,params=params)
with open(path,'wb') as file:
    file.write(response.content)