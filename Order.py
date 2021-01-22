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

def getCapital():
    account = api.get_account()
    capital = account.equity
    return(capital)

