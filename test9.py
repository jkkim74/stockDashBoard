import requests
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import yfinance as yf
from datetime import datetime
import FinanceDataReader as fdr

enddate=datetime.now().strftime('%Y-%m-%d')
kospi=yf.download('^KS11', '2020-01-01', enddate, auto_adjust=True).resample('M').last()


apikey = 'D1S4RQZ081GQX08WPWDC'
url = 'https://ecos.bok.or.kr/api/StatisticSearch/' + apikey \
      + '/json/kr/1/100/901Y067/M/202001/202311'
response = requests.get(url)
result = response.json()
list_total_count = (int)(result['StatisticSearch']['list_total_count'])
list_count = (int)(list_total_count / 100) + 1

rows = []
for i in range(0, list_count):
    start = str(i * 100 + 1)
    end = str((i + 1) * 100)

    url = 'https://ecos.bok.or.kr/api/StatisticSearch/' + apikey + '/json/kr/' \
          + start + '/' + end + '/901Y067/M/202001/202311'
    response = requests.get(url)
    result = response.json()
    rows = rows + result['StatisticSearch']['row']

df = pd.DataFrame(rows)

# datetime type의 date column을 생성하고, DATA_VALUE column을 float으로 변경하겠습니다.
df['datetime']=pd.to_datetime(df['TIME'].str[:4] + '-' + \
                 df['TIME'].str[4:6] + '-01')
df=df.astype({'DATA_VALUE':'float'})


df2=df.loc[df['ITEM_NAME1']=='선행지수순환변동치']

# Retrieve the exchange rate data (KRW/USD) with a monthly frequency
exchange_rate = fdr.DataReader('USD/KRW', '2020-01-01', enddate).resample('M').last()
# 나눠서 그릴 공간 생성
fig = make_subplots(rows=3, cols=1)

# 각 공간에 Trace 채워넣
fig.add_trace(
    go.Scatter(x=kospi.index, y=kospi['Close'], name="KOSPI"),
    row=1, col=1
)
fig.add_trace(
    go.Scatter(x=df2['datetime'], y=df2['DATA_VALUE'], name="선행지수순환변동치"),
    row=2, col=1
)

fig.add_trace(
    go.Scatter(x=exchange_rate.index, y=exchange_rate['Close'], name="Exchange Rate"),
    row=3, col=1
)

fig.update_layout(
    width=800,
    height=600,
    margin_l=50,
    margin_r=50,
    margin_b=100,
    margin_t=100,
    # 백그라운드 칼라 지정, margin 잘 보이게 하기위함
    paper_bgcolor="LightSteelBlue",
)
fig.show()
