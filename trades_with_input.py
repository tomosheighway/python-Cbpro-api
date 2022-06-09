import cbpro
import time 

data = open('cbproapi.txt','r').read().splitlines()
public_key = data[0]
secret_key = data[1]
passphrase = data[2]

auth_client = cbpro.AuthenticatedClient(public_key, secret_key, passphrase)

print("Enter trade pair (BTC-GBP)")
pair = input()

print("Enter Buy Price: ")
buy_price = float(input())
print("Enter buy trade size: ")
buy_trade_size = float(input())
print("Enter Sell Price: ")
sell_price = float(input())
print("Enter sell trade size: ")
sell_trade_size = float(input())

print("Trade pair selected:", pair)
print("Buy price set at:", buy_price)
print("Buy trade size set at:", buy_trade_size)
print("Sell price set at:", sell_price)
print("Sell trade size set at:", sell_trade_size)

while True:
    price = float(auth_client.get_product_ticker(product_id=pair)['price'])
    if price <= buy_price:
        print("buying")
        auth_client.buy(size = buy_trade_size, order_type="market" , product_id=pair)
    elif price >= sell_price:
        print("selling")
        auth_client.sell(size= buy_trade_size, order_type="market" , product_id=pair)
    else:
        print("waiting.... price of",pair,"at:", price)
    time.sleep(10)
