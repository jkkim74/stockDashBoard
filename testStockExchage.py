import FinanceDataReader as fdr
import requests
import json
import matplotlib.pyplot as plt
import pandas as pd
import math

# Download KOSPI index data using FinanceDataReader
kospi_df = fdr.DataReader('KS11', '2019-01-01', '2022-12-01').resample('M').last()

# Download Korean won / US dollar exchange rate data using FinanceDataReader
exchange_rate_df = fdr.DataReader('USD/KRW', '2019-01-01', '2022-12-01').resample('M').last()

# Replace [YOUR_API_KEY] with your own API key
api_key = 'D1S4RQZ081GQX08WPWDC'

# Set the URL with the API key and other parameters
url = f'https://ecos.bok.or.kr/api/StatisticSearch/{api_key}/json/kr/1/1000/901Y067/M/201901/202212/I16E/'

# Make a GET request to the URL and extract the JSON data
response = requests.get(url)
data = json.loads(response.text)

# Extract the cyclical component data
cyclical_component_data = []
for item in data['StatisticSearch']['row']:
    if item['ITEM_NAME1'] == '선행지수순환변동치':
        date = item['TIME']
        value = math.floor(float(item['DATA_VALUE']))
        cyclical_component_data.append((date, value))
print(cyclical_component_data)
# Convert the cyclical component data to a Pandas DataFrame and set the date column as the index
cyclical_component_df = pd.DataFrame(cyclical_component_data, columns=['Date', 'Cyclical Component'])
cyclical_component_df['Date'] = pd.to_datetime(cyclical_component_df['Date'], format='%Y%m')
cyclical_component_df.set_index('Date', inplace=True)
# Combine the three DataFrames into one
combined_df = pd.concat([kospi_df['Close'], exchange_rate_df['Close'], cyclical_component_df], axis=1)
print(combined_df)
# Plot the combined data using matplotlib
fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('Date')
ax1.set_ylabel('KOSPI', color=color)
ax1.plot(combined_df.index, combined_df['Close'], color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()

color1 = 'tab:blue'
ax2.set_ylabel('KRW/USD', color=color1)
ax2.plot(combined_df.index,  combined_df['Close'], color=color1)
ax2.tick_params(axis='y', labelcolor=color1)

ax3 = ax1.twinx()

color2 = 'tab:green'
ax3.spines['right'].set_position(('axes', 1.1))
ax3.set_ylabel('Cyclical Component', color=color2)
ax3.plot(combined_df.index,  combined_df['Cyclical Component'], color=color2)
ax3.tick_params(axis='y', labelcolor=color2)

plt.show()