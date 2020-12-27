import requests
import asyncio
import time
import aiohttp

start = time.time()

host = "http://127.0.0.1:5000/"
urls = ["bobo","jay","tom"]

async def get_page(url):
    # should use aiohttp instead of request
    print("Downloading", url)
    async with aiohttp.ClientSession() as session:
        async with await session.get(url) as resp:
            res = await resp.text()
            print(res)

    

tasks = []
for u in urls:
    c = get_page(host+u)
    tasks.append(asyncio.ensure_future(c))

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
print(end-start)
