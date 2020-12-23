#Method to calculate EMA
import pandas_datareader as web
import datetime

start = datetime.datetime(2018, 1, 1)
end = datetime.datetime(2020, 1, 1)

ticker = "AAPL"

test = web.DataReader(ticker, "yahoo", start, end)

#print(test)

csv_name = ticker + '.csv'

test.to_csv(csv_name)
