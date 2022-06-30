from alpha_vantage.timeseries import TimeSeries

app = TimeSeries() #set up your api key as an environment variable ALPHAVANTAGE_API_KEY

aapl = app.get_daily(symbol='AAPL',outputsize='compact')
print(aapl)