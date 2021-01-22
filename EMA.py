import pandas_datareader as web
import pandas as pd
import datetime

def getEMA(length, csv_name, ticker):

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
    prevEMA = getPrevEMA(length, ticker)
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
    
def getPrevEMA(length, ticker):

    emacsv_name = ticker + 'EMA.csv'
    EMAdata = pd.read_csv(emacsv_name)

    dl = str(length) + ' DAY'
    prevEMAlist = EMAdata.loc[:, dl]
    #print(prevEMAlist)
    
    end = len(prevEMAlist) - 1

    pEMA = prevEMAlist[end]
    return(pEMA)