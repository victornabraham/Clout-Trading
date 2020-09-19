from pyrh import Robinhood
import time

rh = Robinhood()
rh.login(username="clouttrading@gmail.com", password="gojwaT-poxnih-6cacsy")
rh.print_quote("AAPL")
