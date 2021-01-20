import datetime
import pandas as pd
import pandas_datareader as web

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

pricedata = pd.read_csv(csv_name)

acprices = pricedata.loc[:, 'adjusted close']
acprices = acprices.to_list()

emalng = 12 #pass in variable
acptotal = 0

#back to front
start = len(acprices) - 1
end = start - emalng 
#print(acprices)

def getEMA():
    for i in range(start, end, -1):
    acptotal = acprices[i] + acptotal
    #print(acptotal, "\t", i)

    #SMA (intial EMA)
    sma = acptotal / emalng

    mutli = 2 / (acptotal + 1)

    #Closing Price
    acp = acprices(start)

#EMA


if i == start:
    ema = ((acp - sma) * multi) + sma
elif i > start:


else:
    print(ERROR)
    break

#Get Previous EMA
#Get Current EMA from Previous
#Compare
#Buy, Sell, or Hold
