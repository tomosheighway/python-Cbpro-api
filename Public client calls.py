import cbpro

public_client= cbpro.PublicClient()

result = public_client.get_products()  # currency pairs 
result2 = public_client.get_currencies()    # raw currencies 
result3 = public_client.get_time()     #time
result4 = public_client.get_product_order_book('BTC-GBP')       #bids / asks 
result5 = public_client.get_product_ticker('btc-gbp')
result6 = public_client.get_product_24hr_stats('btc-gbp')

eth_trades = public_client.get_product_trades('eth-gbp') # view trades at that time

for row in result2:
    print(row['id'])  

print(result6)



print(next(eth_trades))
print(next(eth_trades))
print(next(eth_trades))