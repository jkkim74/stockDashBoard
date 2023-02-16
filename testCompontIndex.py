import requests
import json
import pandas as pd

# Replace [YOUR_API_KEY] with your own API key
api_key = 'D1S4RQZ081GQX08WPWDC'

# Set the URL with the API key and other parameters
url = f'http://ecos.bok.or.kr/api/StatisticSearch/{api_key}/json/kr/1/300/901Y067/M/200001/202212/I16E/'

# Make a GET request to the URL and extract the JSON data
response = requests.get(url)
data = json.loads(response.text)
print(data)
# Extract the cyclical component data
for item in data['StatisticSearch']['row']:
    if item['ITEM_NAME1'] == '선행지수순환변동치':
        leading_index = item['DATA_VALUE']
        df = pd.r
    elif item['ITEM_NAME1'] == '지수순환변동치':
        cyclical_component = item['DATA_VALUE']

# Print the extracted data
print('Leading Index:', df)
# print('Cyclical Component:', cyclical_component)
