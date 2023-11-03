
from datetime import datetime
import pandas as pd
import talib
#from pandas_datareader import data as web
import FinanceDataReader as fdr
import numpy as np

# row 생략 없이 출력
pd.set_option('display.max_rows', None)
# col 생략 없이 출력
pd.set_option('display.max_columns', None)
np.set_printoptions(threshold=np.inf, linewidth=np.inf)

# Asserts that yahoo is minimally working
tsl_df = fdr.DataReader('TSLA','2023-01-01','2023-11-01') #테슬라 주가

#이동평균선 계산하기
tsl_df['SMA'] = talib.SMA(tsl_df['Close'], timeperiod = 20)

#상대강도지수 계산하기
tsl_df['RST'] = talib.RSI(tsl_df['Close'], timeperiod = 14)

#결과출력
print(tsl_df.tail())
