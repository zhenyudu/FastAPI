import asyncio
import aiohttp
import time

async def send_request(session, url):
    async with session.get(url) as response:
        return await response.json()
    
async def main(sub_url):
    url = "http://127.0.0.1:8000"+sub_url
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = [send_request(session, url) for _ in range(5)]
        responses = await asyncio.gather(*tasks)
        for response in responses:
            pass
    print(f"{url}")
    print(time.time()-start_time)


if __name__ == "__main__":

    # print(asyncio.run(main('/root/1/')))
    # print(asyncio.run(main('/root/2/')))
    # print(asyncio.run(main('/root/3/')))
    # print(asyncio.run(main('/root/4/')))
    print(asyncio.run(main('/cal/1/')))
    print(asyncio.run(main('/cal/2/')))