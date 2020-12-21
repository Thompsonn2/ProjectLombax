import alpaca_trade_api as tradeapi

#Config file
api = tradeapi.REST(
    base_url = 'https://paper-api.alpaca.markets', #Paper Trading Url
    key_id = 'PK3B4AH8O4PKD0ZM3LPG',
    secret_key = 'ZkKtDZaJvWYqplI0K9Jm4hmZZ365WAhK8IzPzCk8'
)

def submit_buy_order(ticker, shares):
    #print('BUY')
    api.submit_order(
        symbol = ticker,
        qty = shares,
        side = 'buy',
        type = 'market',
        time_in_force = 'gtc'
        #Order summary
    )

def submit_sell_order(ticker, shares):
    #print('SELL')
    api.submit_order(
        symbol = ticker,
        qty = shares, 
        side = 'sell',
        type = 'market',
        time_in_force = 'gtc'
        #Order summary
    )

def main():
    while 0 != 1:
        var1 = int(input('Submit trade: Press 1 to Buy or 2 to Sell. To exit press any other number \n'))
        if var1 != 1 and var1 != 2:
            break
        ticker = input('Enter the companies stock ticker: \n')
        num_shares = int(input('Enter the number of shares for this transaction: \n'))
        if var1 == 1:
            submit_buy_order(ticker, num_shares)
        elif var1 == 2:
            submit_sell_order(ticker, num_shares)
        else:
            print('ERROR')
            break
    
main()