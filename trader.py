import robin_stocks.robinhood as rs
import os

robin_user = os.environ.get("robinhood_username")
robin_pass = os.environ.get("robinhood_password")

rs.login(username= robin_user,
         password= robin_pass,
         expiresIn=86400,
         by_sms=True)

ticker = "NVDA"
amount = 100

order = rs.orders.order_buy_fractional_by_price(symbol = ticker,
                                       amountInDollars = amount,) 
print("BOT: Groomstone has bought " + order['quantity'] + " of " + ticker +  " at " + order['price'] + ".")

# positions = rs.account.get_all_positions()
# print(positions)

rs.logout()