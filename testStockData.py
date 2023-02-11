import pandas as pd
import matplotlib.pyplot as plt
import FinanceDataReader as fdr

plt.rcParams["font.family"] = 'nanummyeongjo'
plt.rcParams["figure.figsize"] = (14,4)
plt.rcParams['lines.linewidth'] = 2
plt.rcParams["axes.grid"] = True


# 애플(AAPL), 2017년
# df = fdr.DataReader('AAPL', '2017')
# df['Close'].plot()

#plt.plot(df['Close'])
# 원달러 환율, 1995년~현재
# df = fdr.DataReader('USD/KRW', '2020')
# df['Close'].plot()
plt.show()

# 애플(AAPL), 2018-01-01 ~ 2018-03-30
# df = fdr.DataReader('AAPL', '2018-01-01', '2018-03-30')
# df.tail()

# S&P 500 종목 전체
df_spx = fdr.StockListing('S&P500')
print(df_spx)