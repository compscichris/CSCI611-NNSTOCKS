import sys

from alpaca_trade_api.rest import REST, TimeFrame, TimeFrameUnit

stock_name = "AAPL"

api = REST('PKJ41QP5QU0TYS4S1BYB', 'o5HVFGx0XWSMoMyeQdRJwG1apYXtuMNcguWpjqqe')

bar_iter = api.get_bars(stock_name, TimeFrame(15, TimeFrameUnit.Minute), "2021-06-08", "2024-06-09", adjustment='raw').df
#api = REST()
#api.get_trades("AAPL", "2021-06-08", "2021-06-08", limit=10).df


#print(bar_iter.close)

data = []

for i in bar_iter:
    data.append(i.close)

for i in data:
    print(i)

import numpy as np
arr = np.array(data)
np.save(stock_name + '.npy', arr)   