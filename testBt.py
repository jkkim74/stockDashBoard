import bt
import pandas as pd
import matplotlib.pyplot as plt


plt.rcParams["font.family"] = 'nanummyeongjo'
plt.rcParams["figure.figsize"] = (14,4)
plt.rcParams['lines.linewidth'] = 2
plt.rcParams["axes.grid"] = True

#Fetch some data
data = bt.get('aapl',start='2010-01-01')

#create a signal
sma = data.rolling(50).mean()
signal = data > sma

#Define the strategy
bt_strategy = bt.Strategy('AboveSMA',
    [
        bt.algos.RunMonthly(),
        bt.algos.SelectWhere(signal),
        bt.algos.WeighEqually(),
        bt.algos.Rebalance()
    ]
)

#create a backtest
bt_test = bt.Backtest(bt_strategy,data)

#Run th backtest
results = bt.run(bt_test)

#Plot ther results
results.plot()

#Plot the buy/sell signals
buy_signals = signal.apply(lambda x: data['aapl'] * x)
sell_signals = signal.apply(lambda x: data['aapl'] * (1 - x))
buy_signals[buy_signals == 0] = None
sell_signals[sell_signals == 0] = None

plt.plot(buy_signals,marker='*',markersize=1, color='g',linestyle='None')
plt.plot(sell_signals,marker='v',markersize=1, color='r',linestyle='None')
plt.show()