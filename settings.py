import os



API_KEY = os.getenv('ALPHAVANTAGE_API_KEY')
API_URL = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}'
SYMBOLS = ['AAPL', 'GOOG', 'TSLA', 'MSFT']
