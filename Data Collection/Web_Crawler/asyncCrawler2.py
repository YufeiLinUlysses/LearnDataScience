import asyncio
import time
urls = ["www.baidu.com", "www.sogou.com", "www.goubanjia.com"]

# Cannot use sync models in async
async def makeRequest(url):
    print("Requesting: ", url)
    await asyncio.sleep(2)
    print("Succeded")
    return url

# Get the instance returned from an async function
# c = makeRequest("www.baidu.com")

# Establish event loop
# loop = asyncio.get_event_loop()

# register the instance into loop
# loop.run_until_complete(c)

# # using task, depend on loop
# loop = asyncio.get_event_loop()
# # establish a task instance
# task = loop.create_task(c)
# print(task)

# loop.run_until_complete(task)

# print(task)

# using future, does not depend on loop
# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(c)
# print(task)
# loop.run_until_complete(task)
# print(task)

def callbackFunc(task):
    print(task.result())

# Initate multiple task instances
tasks = []
for u in urls:
    c = makeRequest(u)
    tasks.append(asyncio.ensure_future(c))


loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(c)
# callback
# task.add_done_callback(callbackFunc)
loop.run_until_complete(asyncio.wait(tasks))
