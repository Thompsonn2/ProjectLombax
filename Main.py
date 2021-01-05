import pandas_datareader as web
import pandas as pd
import datetime

from EMA import *

start = datetime.datetime(2018, 1, 1)
end = datetime.datetime(2020, 1, 1)

API_KEY = '8YUCTMX2NCJUI70T'

ticker = 'AAPL'

test = web.DataReader(ticker, 'av-daily-adjusted', start, end, api_key = API_KEY)
#print(test)

csv_name = ticker + '.csv'

test.to_csv(csv_name)

getEMA(csv_name)