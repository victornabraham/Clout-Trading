from pyrh import Robinhood
import time

rh = Robinhood()
rh.login
rh.print_quote("AAPL")
