import pandas


import pandas_datareader as pdr
import datetime

aapl = pdr.get_data_yahoo('AAPL',
                          start=datetime.datetime(2019, 1, 1),
                          end=datetime.datetime(2019, 2, 19))

print(aapl)
