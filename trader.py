import robin_stocks.robinhood as rs
import os

robin_user = os.environ.get("robinhood_username")
robin_pass = os.environ.get("robinhood_password")

rs.login(username= robin_user,
         password= robin_pass,
         expiresIn=86400,
         by_sms=True)

rs.account.get_all_positions()

rs.logout()