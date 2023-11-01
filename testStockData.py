import pandas as pd
import matplotlib.pyplot as plt
import FinanceDataReader as fdr
import json
import numpy as np

# row 생략 없이 출력
pd.set_option('display.max_rows', None)
# col 생략 없이 출력
pd.set_option('display.max_columns', None)
np.set_printoptions(threshold=np.inf, linewidth=np.inf)
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
# exchange_rate = df['Close'].plot()
#
# # KS11 (KOSPI 지수), 2015년~현재
# df2 = fdr.DataReader('KS11', '2015')
# kospi_index = df2['Close'].plot()
#
# t1 = np.arange(900, 4000, 1)
# t2 = np.arange(900, 4000, 1)
#
# plt.plot(t1, exchange_rate, t2, kospi_index, 'r-')
#
# plt.show()
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
# df_spx = fdr.StockListing('S&P500')
# #df_spx.head()
# #print(len(df_spx))
# print(df_spx.head())
#df = fdr.DataReader('001250','2018') # GS글로벌 2018년
#df = fdr.DataReader('AAPL','2023-01-01','2023-10-31') # 애플주가
#df = fdr.DataReader('USD/KRW','2023') # 환율
# df = fdr.DataReader('BTC/KRW','2023') # 비트코인
tsl_df = fdr.DataReader('TSLA','2023-01-01','2023-11-01') #테슬라 주가
# print(df.tail(10))
# df['Close'].plot()
#
# plt.show()
tsl_df['Close_lag']= tsl_df['Close'].shift() # 전날에 종가
tsl_df['pct_change']= tsl_df['Close'].pct_change() # 전날종가와 현재종가의 변화 율
tsl_df['close_diff']= tsl_df['Close'].diff() # 현재종가 - 전날종가
tsl_df['MX'] = tsl_df['Close'].rolling(window=5).mean()
print(tsl_df.head(10))
