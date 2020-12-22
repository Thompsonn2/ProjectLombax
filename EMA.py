#Method to calculate EMA
import pandas.io.data as web
import datetime

start = datetime.datetime(2018, 1, 1)
end = datetime.datetime(2020, 1, 1)

test = web.DataReader("AAPL", "yahoo", start, end)

print(test)
