import requests
import json

# Replace [YOUR_API_KEY] with your own API key
api_key = 'D1S4RQZ081GQX08WPWDC'

# Set the URL with the API key and other parameters
url = 'http://ecos.bok.or.kr/api/StatisticSearch/{api_key}/json/kr/1/10/036Y001/DD/20000101/20211231/0000001/'

# Make a GET request to the URL and extract the JSON data
response = requests.get(url)
print(response)
data = json.loads(response.text)
print(data)
# Extract the cyclical component data
for item in data['StatisticSearch']['row']:
    if item['ITEM_NAME1'] == '종합순환지수':
        leading_index = item['DATA_VALUE']
    elif item['ITEM_NAME1'] == '지수순환변동치':
        cyclical_component = item['DATA_VALUE']

# Print the extracted data
print('Leading Index:', leading_index)
print('Cyclical Component:', cyclical_component)
