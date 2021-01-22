import datetime
import pandas as pd
import pandas_datareader as web

from EMA import *
from datetime import date, timedelta

today = date.today()
#print("Todays date is:", today)

prevdate = (date.today() - timedelta(days = 50)).isoformat()
#print("\nPrevious date is:", prevdate)

API_KEY = '8YUCTMX2NCJUI70T'

ticker = 'AAPL'
test = web.DataReader(ticker, 'av-daily-adjusted', prevdate, today, api_key = API_KEY)
csv_name = ticker + '.csv'
test.to_csv(csv_name)
#print(test)

ema26 = getEMA(26, csv_name, ticker)
ema12 = getEMA(12, csv_name, ticker)
ema9 = getEMA(9, csv_name, ticker)

print(ema26, ema12, ema9)

#Read previous EMA from csv file
pema26 = getPrevEMA(26, ticker)
pema12 = getPrevEMA(12, ticker)
pema9 = getPrevEMA(9, ticker)

print(pema26, pema12, pema9)

#Write current date and EMAs to csv file
#Compare (Buy, Sell, or Hold)
#Email Result

