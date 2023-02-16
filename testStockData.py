import pandas as pd
import matplotlib.pyplot as plt
import FinanceDataReader as fdr
import json
import numpy as np

# plt.rcParams["font.family"] = 'nanummyeongjo'
# plt.rcParams["figure.figsize"] = (14,4)
# plt.rcParams['lines.linewidth'] = 2
# plt.rcParams["axes.grid"] = True


# 애플(AAPL), 2017년
# df = fdr.DataReader('AAPL', '2017')
# df['Close'].plot()

#plt.plot(df['Close'])
# 원달러 환율, 1995년~현재
df = fdr.DataReader('USD/KRW', '2020')
exchange_rate = df['Close'].plot()

# KS11 (KOSPI 지수), 2015년~현재
df2 = fdr.DataReader('KS11', '2015')
kospi_index = df2['Close'].plot()

t1 = np.arange(900, 4000, 1)
t2 = np.arange(900, 4000, 1)

plt.plot(t1, exchange_rate, t2, kospi_index, 'r-')

plt.show()
# print(df['Close'])
# print(type(df))
# result = df.to_json(orient="values")
# parsed = json.loads(result)
# result2 = json.dumps(parsed,indent=3)
# print(result2)
# # 애플(AAPL), 2018-01-01 ~ 2018-03-30
# # df = fdr.DataReader('AAPL', '2018-01-01', '2018-03-30')
# # df.tail()
#
# # S&P 500 종목 전체
# # df_spx = fdr.StockListing('S&P500')
# # print(df_spx)