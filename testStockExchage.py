import FinanceDataReader as fdr
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.filters.hp_filter import hpfilter
import requests
import json

# Get historical KOSPI index data
kospi = fdr.DataReader('KS11', '2000-01-01')

# Get historical USD/KRW exchange rate data
usd_krw = fdr.DataReader('USD/KRW', '2000-01-01')

# # Get cyclical component of the leading index from Bank of Korea
# bok = pd.read_html('https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_1C8013&conn_path=', header=0, index_col=0)[0]
# print(bok)
# bok.index = pd.to_datetime(bok.index)
# print(bok)
# bok = bok['종합순환지수']['월별']
# bok_cycle, bok_trend = hpfilter(bok, lamb=129600)

# Replace [YOUR_API_KEY] with your own API key
api_key = 'D1S4RQZ081GQX08WPWDC'

# Set the URL with the API key and other parameters
url = f'http://ecos.bok.or.kr/api/StatisticSearch/{api_key}/json/kr/1/10/036Y001/DD/20000101/20211231/0000001/'

# Make a GET request to the URL and extract the JSON data
response = requests.get(url)
data = json.loads(response.text)
print(data)
# Extract the cyclical component data
for item in data['StatisticSearch']['row']:
    if item['ITEM_NAME1'] == '종합순환지수':
        leading_index = item['DATA_VALUE']
    elif item['ITEM_NAME1'] == '지수순환변동치':
        cyclical_component = item['DATA_VALUE']

bok_cycle, bok_trend = hpfilter(cyclical_component, lamb=129600)

# Print the extracted data

# Plot all three on the same graph
fig, ax1 = plt.subplots()
ax1.plot(kospi.index, kospi['Close'], 'b-', label='KOSPI')
ax1.set_xlabel('Date')
ax1.set_ylabel('KOSPI Index', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.plot(usd_krw.index, usd_krw['Close'], 'r-', label='USD/KRW')
ax2.set_ylabel('USD/KRW Exchange Rate', color='r')
ax2.tick_params('y', colors='r')

ax3 = ax1.twinx()
ax3.spines['right'].set_position(('axes', 1.1))
ax3.plot(bok_cycle.index, bok_cycle, 'g-', label='Cyclical Component of Leading Index')
ax3.set_ylabel('Cyclical Component of Leading Index', color='g')
ax3.tick_params('y', colors='g')

plt.legend()
plt.show()