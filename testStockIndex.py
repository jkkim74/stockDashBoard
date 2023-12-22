import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import pandas_datareader as pdr

# 데이터 소스에서 데이터 불러오기
start_date = datetime(2010, 1, 1)
end_date = datetime(2023, 1, 1)

# 원달러 환율 데이터
exchange_rate = pdr.get_data_yahoo("KRW=X", start_date, end_date)['Adj Close']

# 미국 10년물 국공채 금리 데이터
bond_yield = pdr.get_data_fred("GS10", start_date, end_date)

# 선행지수 순환변동치 데이터
leading_index = pdr.get_data_fred("USSLIND", start_date, end_date)

# 코스피지수 데이터
kospi = pdr.get_data_yahoo("^KS11", start_date, end_date)['Adj Close']

# 데이터를 하나의 데이터프레임으로 합치기
data = pd.DataFrame({
    'Exchange Rate': exchange_rate,
    'Bond Yield': bond_yield['GS10'],
    'Leading Index': leading_index['USSLIND'],
    'KOSPI Index': kospi
})

# 그래프 그리기
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))

for i, (col, ax) in enumerate(zip(data.columns, axes.flatten())):
    ax.plot(data.index, data[col], label=col)
    ax.set_title(col)
    ax.legend()

plt.tight_layout()
plt.show()