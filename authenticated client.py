import cbpro 

data = open('cbproapi.txt','r').read().splitlines()

public_key = data[0]
secret_key = data[1]
passphrase = data[2]

auth_client = cbpro.AuthenticatedClient(public_key, secret_key, passphrase)

#limit buy
print(auth_client.buy(price="10.0", size="10.1" ,order_type="limit", product_id="ETH-GBP"))     
#market buy
print(auth_client.buy(size="10", order_type= "market", product_id="ETH-GBP"))      

#limit sell
print(auth_client.sell(price="200000.0", size="0.1" ,order_type="limit", product_id="ETH-GBP"))  
#market sell
print(auth_client.sell(size="10", order_type= "market", product_id="ETH-GBP"))  

#alt methods of buy /sell 
print(auth_client.place_limit_order(product_id="BTC-GBP", side="buy", price="10.00", size="1.0"))
print(auth_client.place_market_order(product_id="BTC-GBP", side="buy", size="1.0"))

#canceling orders 
print(auth_client.cancel_all(product_id="BTC-GBP"))

#getting orders
print(auth_client.get_orders(product_id="BTC-ETH"))

import time 
sell_price = 300000
sell_amount= 0.3
buy_price= 1600
buy_amount = 0.2

 

#basic trading off a price automated to check every 5 seconds 
while True:
    price = float(auth_client.get_product_ticker(product_id="BTC-GBP")['price'])
    if price <= buy_price:
        print("buying")
        auth_client.buy(size = buy_amount, order_type="market" , product_id="BTC-GBP")
    elif price >= sell_price:
        print("selling")
        auth_client.sell(size= buy_amount, order_type="market" , product_id="BTC-GBP")
    else:
        print("nothing... price at:", price)
    time.sleep(5)