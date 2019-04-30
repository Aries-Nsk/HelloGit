from moex import MOEX
moex = MOEX()
data = moex.history_engines_stock_totals_securities(date_start='2018-01-01', date_end='2018-08-16', secid=['SBER'])

data[["SYSTIME", "SECID", "OPEN", "CLOSE", "LOW", "HIGH", "VOLUME"]]

print(data)
