from time import time
import asyncio
from unittest import result
import aiohttp
import blog_spider

sem = asyncio.Semaphore(10)

async def async_craw(url):
    async with sem:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                result = await resp.text()
                await asyncio.sleep(5)
                print(f'craw url: {url}, {len(result)}')

loop = asyncio.get_event_loop()

tasks = [
    loop.create_task(async_craw(url))
    for url in blog_spider.urls
]

start = time()
loop.run_until_complete(asyncio.wait(tasks))
end = time()
print('use time seconds: ', end-start)