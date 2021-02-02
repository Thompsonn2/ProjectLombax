import pandas_datareader as web
import pandas as pd
import datetime

def getMACDEMA(csv_name, ticker):

    length = 9
    pricedata = pd.read_csv(csv_name)

    acprices = pricedata.loc[:, 'adjusted close']
    acprices = acprices.to_list()

    back = len(acprices) - 1
    front = back - length

    acptotal = 0

    for i in range(back, front, -1):
        acptotal = acprices[i] + acptotal
        #print(acptotal, "\t", i)

    #Previous EMA
        #(Call getPrevEMA Function)
    prevEMA = getPrevMACDEMA(length, ticker)
    #print(prevEMA)

    #Multiplier
    multi = 2 / (acptotal + 1)
    #print(multi)

    #Closing Price
    acp = acprices[back]
    #print(acp)

    #EMA
    ema = ((acp - prevEMA) * multi) + prevEMA
    #print(ema)
    return(ema)
    
def getPrevMACDEMA(ticker):
    length = 9

    emacsv_name = ticker + 'EMA.csv'
    EMAdata = pd.read_csv(emacsv_name)

    dl = str(length) + ' DAY MACD'
    prevEMAlist = EMAdata.loc[:, dl]
    #print(prevEMAlist)
    
    end = len(prevEMAlist) - 1

    pEMA = prevEMAlist[end]
    return(pEMA)