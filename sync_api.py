import time
import requests
from settings import API_URL, API_KEY, SYMBOLS



results = []

start = time.time()
for symbol in SYMBOLS:
    print(f'Working on symbol {symbol}')
    response = requests.get(API_URL.format(symbol, API_KEY))
    results.append(response.json())
end = time.time()
total_time = end - start

print(f'It took {total_time} seconds to make {len(SYMBOLS)} API calls synchronously.')
