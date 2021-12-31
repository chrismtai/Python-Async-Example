# Python-Sync-Async-Examples

## Quickstart

```bash
git clone https://github.com/f3600011/Python-Async-Example
cd Python-Async
pip install -r requirements.txt
```
Get a free API key from [Alpha Vantage](https://www.alphavantage.co/support/#api-key) and set it as an [environment variable](https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html). If you're unfamiliar with environment variables, set it in your `.env` file.

```bash
export ALPHAVANTAGE_API_KEY='YOUR KEY HERE'
```

The free Alpha Vantage API key is rate limited to 5 API calls/minute. If you'd like to speed test APIs, you can swap it out for a different API, like [this json dummy api.](https://jsonplaceholder.typicode.com/)

Then run:
```
python sync_api.py
```
And you'll get an output like:
```
It took 4.341384410858154 seconds to make 4 API calls synchronously.
```

To run it async, run:
```
python async_api.py 
```
and you'll get an output like:
```
It took 0.400589227676391 seconds to make 4 API calls asynchronously.
```

You can add more api calls by adding more markets in settings.py file
```
SYMBOLS = ['PFE', 'GOOG', 'TSLA', 'MSFT', 'SBUX', 'NFLX']
```
