#Method to calculate EMA
import pandas_datareader as web
import pandas as pd
import datetime

def getEMA(csv_name, length):

    pricedata = pd.read_csv(csv_name)

    acprices = pricedata.loc[:,'adjusted close']
    dates = pricedata.loc[:, 'Unnamed: 0']
    #print(acprices)
    #print(dates)
    

    acprices = acprices.to_list()
    dates = dates.to_list()
    #print(acprices)
    #print(dates)

    strt = 0
    end = length
    emalist = []

    #len(acprices)
    while end <= len(acprices):

        emalng = length
        acptotal = 0

        #SMA (intial EMA)
        for i in range(strt, end):
            acptotal = acprices[i] + acptotal

        sma = acptotal / emalng

        #Multiplier
        multi = 2 / (acptotal + 1)

        #Closing Price
        acp = acprices[end - 1]

        #EMA
        if strt == 0:
            ema = ((acp - sma) * multi) + sma
            #print(ema, "\t\t", strt, end)
        elif strt > 0:
            prevema = emalist[-1]
            ema = ((acp - prevema) * multi) + prevema
            #print("26 day Sum: ", acptotal)
            #print("Multiplier: ", multi)
            #print("Adj Close: ", acp)
            #print("Previous EMA: ", prevema)
            #print(ema, "\t\t", strt, end)

        emalist.append(ema)
        strt = strt + 1
        end = end + 1
    
    return(emalist)

        









