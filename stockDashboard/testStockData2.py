import yfinance as yf
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd

# 경제 지표 데이터 가져오기
def get_economic_data():
    # 선행지수순화변동치 (Leading Index for Korea)
    leading_index = yf.download('KOEAPYIYIndex', start='2010-01-01', end='2023-01-01')['Adj Close']

    # KOSPI 지수
    kospi_index = yf.download('^KS11', start='2010-01-01', end='2023-01-01')['Adj Close']

    economic_data = pd.concat([leading_index, kospi_index], axis=1)
    economic_data.columns = ['Leading Index', 'KOSPI Index']
    return economic_data

# 대시보드 앱 생성
app = dash.Dash(__name__)

# 경제지표 데이터 가져오기
economic_data = get_economic_data()

# 대시보드 레이아웃 정의
app.layout = html.Div([
    html.H1("경기 선행지수와 KOSPI 지수 비교 대시보드"),
    dcc.Graph(
        id='economic-chart',
        figure={
            'data': [
                {'x': economic_data.index, 'y': economic_data['Leading Index'], 'type': 'line', 'name': 'Leading Index'},
                {'x': economic_data.index, 'y': economic_data['KOSPI Index'], 'type': 'line', 'name': 'KOSPI Index'},
            ],
            'layout': {
                'title': '경기 선행지수와 KOSPI 지수 비교',
                'xaxis': {'title': '날짜'},
                'yaxis': {'title': '값'},
            }
        }
    ),
])

if __name__ == '__main__':
    app.run_server(debug=True)