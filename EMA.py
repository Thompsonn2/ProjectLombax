#Method to calculate EMA
import pandas_datareader as web
import pandas as pd
import datetime

start = datetime.datetime(2018, 1, 1)
end = datetime.datetime(2020, 1, 1)

API_KEY = '8YUCTMX2NCJUI70T'

ticker = 'AAPL'

test = web.DataReader(ticker, 'av-daily-adjusted', start, end, api_key = API_KEY)
#print(test)

csv_name = ticker + '.csv'

test.to_csv(csv_name)

pricedata = pd.read_csv(csv_name)

acprices = pricedata.loc[:,'adjusted close']
#print(acprices)

#12 Day EMA

emalng = 12
acptotal = 0

#12 Day SMA (intial EMA)
for i in range(emalng):
    acptotal = acprices[i] + acptotal

sma = acptotal / emalng
print(sma)

#Multiplier
multi = 2 / (acptotal + 1)
print(multi)

#Closing Price
acp = acprices[emalng - 1]
print(acp)

#EMA
ema = ((acp - sma) * multi) + sma
print(ema)







