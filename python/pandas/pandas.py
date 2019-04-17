import python.pandas


#import pandas_datareader as pdr
#import datetime

from pandas_datareader import data, wb
from datetime import date

# aapl = pdr.get_data_yahoo('AAPL',
#                           start=datetime.datetime(2019, 1, 1),
#                           end=datetime.datetime(2019, 2, 19))
#
# print(aapl)

start = date(2012, 1, 1)
end = date(2019, 12, 31)
df = data.DataReader('GE', 'yahoo', start, end)

print(df)
