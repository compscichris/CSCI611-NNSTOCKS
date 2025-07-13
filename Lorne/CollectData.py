import sys

from alpaca_trade_api.rest import REST, TimeFrame, TimeFrameUnit

api = REST('PKJ41QP5QU0TYS4S1BYB', 'o5HVFGx0XWSMoMyeQdRJwG1apYXtuMNcguWpjqqe')

bar_iter = api.get_bars("AAPL", TimeFrame(15, TimeFrameUnit.Minute), "2021-06-08", "2024-06-09", adjustment='raw').df
#api = REST()
#api.get_trades("AAPL", "2021-06-08", "2021-06-08", limit=10).df


#print(bar_iter.close)

data = []

for i in bar_iter.close:
    data.append(float(i))

#for i in data:
#    print(sys.prefix)

import numpy as np
arr = np.array(data)
np.save('my_array.npy', arr)   