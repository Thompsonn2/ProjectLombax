import datetime
import pandas as pd
import pandas_datareader as web

from datetime import date, timedelta
from csv import writer

from EMA import *
from Order import *

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
print(ema26, ema12)

#Read previous EMA from csv file
#Write current date and EMAs to csv file
pema26 = getPrevEMA(26, ticker)
pema12 = getPrevEMA(12, ticker)

emacsv_name = ticker + 'EMA.csv'
new_row = [today, ema26, ema12]
with open(emacsv_name, 'a') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(new_row)
        f_object.close()

macd = ema12 - ema26
signalline = 0 #9 day EMA of macd
print(macd, signalline)
bos = 0 #alpaca

#Buy sell or hold # of shares based on algo

equity = getCapital()
pricedata = pd.read_csv(csv_name)
acprices = pricedata.loc[:, 'adjusted close']
back = len(acprices) - 1
acp = acprices[back]

if signalline < macd and bos == 0: #alpaca
    shares = int(equity / acp)
    submit_buy_order(ticker, shares)
    bos = 1 #alpaca
    print('buy')

if signalline > macd and bos == 1: #alpaca
    shares = 0
    submit_sell_order(ticker, shares)
    bos = 0 #alpaca
    print('sell')


#Compare (Buy, Sell, or Hold)
#Email Result

