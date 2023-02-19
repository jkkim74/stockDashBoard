import requests
import pandas as pd
import yfinance as yf
from datetime import datetime

#선행지수 및 동행지수 순환 변동치는 STAT_CODE=901Y067(8.1.2. 경기종합지수)에서 확인이 가능합니다.
#월 단위로 데이터를 제공하고 있는데 2000년 1월 ~ 2022년 12월까지의 데이터를 수집하겠습니다.
apikey = 'D1S4RQZ081GQX08WPWDC'
url = 'https://ecos.bok.or.kr/api/StatisticSearch/' + apikey \
      + '/json/kr/1/100/901Y067/M/202201/202302'
response = requests.get(url)
result = response.json()
list_total_count = (int)(result['StatisticSearch']['list_total_count'])
list_count = (int)(list_total_count / 100) + 1

rows = []
for i in range(0, list_count):
    start = str(i * 100 + 1)
    end = str((i + 1) * 100)

    url = 'https://ecos.bok.or.kr/api/StatisticSearch/' + apikey + '/json/kr/' \
          + start + '/' + end + '/901Y067/M/202201/202302'
    response = requests.get(url)
    result = response.json()
    rows = rows + result['StatisticSearch']['row']

df = pd.DataFrame(rows)

# datetime type의 date column을 생성하고, DATA_VALUE column을 float으로 변경하겠습니다.
df['datetime']=pd.to_datetime(df['TIME'].str[:4] + '-' + \
                 df['TIME'].str[4:6] + '-01')
df=df.astype({'DATA_VALUE':'float'})

# 수집 데이터중에서 선행지수순환변동치와 동행지수순환변동치만 따로 저장하겠습니다.
df1=df.loc[df['ITEM_NAME1']=='동행지수순환변동치']
df2=df.loc[df['ITEM_NAME1']=='선행지수순환변동치']
print((df2['datetime'], df2['DATA_VALUE']))
# # 그래프로 확인해볼까요
import plotly.graph_objects as go
from plotly.subplots import make_subplots

fig = make_subplots(specs=[[{"secondary_y":True}]])

fig.add_trace(
    go.Scatter(x=df1['datetime'], y=df1['DATA_VALUE'], name="동행지수순환변동치"),
    secondary_y=False,
)

fig.add_trace(
    go.Scatter(x=df2['datetime'], y=df2['DATA_VALUE'], name="선행지수순환변동치"),
    secondary_y=True,
)

fig.update_layout(
    title_text='선행지수순환변동치와 동행지수순환변동치',
    title={'x':0.5, 'y':0.9}
)


# 선행지수 및 동행지수와 KOSPI
# 우선 KOSPI 데이터를 수집하겠습니다.
enddate=datetime.now().strftime('%Y-%m-%d')
kospi=yf.download('^KS11', '2022-01-01', enddate, auto_adjust=True).resample('M').last()
## print(kospi.index,kospi['Close'])

import FinanceDataReader as fdr

# Retrieve the exchange rate data (KRW/USD) with a monthly frequency
exchange_rate = fdr.DataReader('USD/KRW', '2022-01-01', enddate).resample('M').last()
# 선행지수순환변동치
fig = make_subplots(specs=[[{"secondary_y":True}]])

fig.add_trace(
    go.Scatter(x=df2['datetime'], y=df2['DATA_VALUE'], name="선행지수순환변동치"),
    secondary_y=False,
)

fig.add_trace(
    go.Scatter(x=kospi.index, y=kospi['Close'], name="KOSPI"),
    secondary_y=True,
)

fig.add_trace(
    go.Scatter(x=exchange_rate.index, y=exchange_rate['Close'], name="Exchange Rate"),
    secondary_y=True,
)

fig.update_layout(
    title_text='선행지수순환변동치와 코스피',
    title={'x':0.5, 'y':0.9}
)

# 동행지수 순환 변동치
# fig = make_subplots(specs=[[{"secondary_y":True}]])
#
# fig.add_trace(
#     go.Scatter(x=df1['datetime'], y=df1['DATA_VALUE'], name="동행지수순환변동치"),
#     secondary_y=False,
# )
#
# fig.add_trace(
#     go.Scatter(x=kospi.index, y=kospi['Close'], name="KOSPI"),
#     secondary_y=True,
# )
#
# fig.update_layout(
#     title_text='동행지수순환변동치 코스피',
#     title={'x':0.5, 'y':0.9}
# )

fig.show()