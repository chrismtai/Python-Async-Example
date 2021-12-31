import time
import asyncio
import aiohttp
from settings import API_URL, API_KEY, SYMBOLS



results = []

def get_tasks(session):
    tasks = []
    for symbol in SYMBOLS:
        tasks.append(asyncio.create_task(session.get(API_URL.format(symbol, API_KEY), ssl=False)))
    return tasks

async def get_symbols():
    async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session)
        responses = await asyncio.gather(*tasks)
        for response in responses:
            results.append(await response.json())

start = time.time()
asyncio.run(get_symbols())
end = time.time()
total_time = end - start

print(f'It took {total_time} seconds to make {len(SYMBOLS)} API calls asynchronously.')