import robin_stocks.robinhood as rs
import os

robin_user = os.environ.get("robin_user")
robin_pass = os.environ.get("robin_pass")

tickers = []

rs.login(username= robin_user,
         password= robin_pass,
         expiresIn=86400,
         by_sms=True)

get_positions = rs.build_holdings()
print(get_positions)
get_user = rs.build_user_profile()
print(get_user)
cash = get_user['cash']

f = open("champions.txt","r")
for x in f:
    tickers.append(x.strip())

for x in tickers:
    order = rs.orders.order_buy_fractional_by_price(symbol = x,
                                                    amountInDollars = cash/8,) 
    print("BOT: Groomstone has bought " + order['quantity'] + " of " + x +  " at " + order['price'] + ".")

rs.logout()