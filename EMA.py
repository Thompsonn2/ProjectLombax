#Method to calculate EMA
import pandas_datareader as web
import datetime

start = datetime.datetime(2018, 1, 1)
end = datetime.datetime(2020, 1, 1)

API_KEY = '8YUCTMX2NCJUI70T'

ticker = 'AAPL'

test = web.DataReader(ticker, 'av-daily-adjusted', start, end, api_key = API_KEY)

#print(test)

csv_name = ticker + '.csv'

print(test)

test.to_csv(csv_name)
