
## 同步轉異步多線程並發
```python
#CPU型任務
import asyncio
from concurrent.futures import ProcessPoolExecutor

async def afunc():
    print("connect!")
    loop = asyncio.get_event_loop()
    with ProcessPoolExecutor() as pool:
        response = await loop.run_in_executor(pool, func)
    print("success!")
    return response
    

#GPU型任務
import asyncio
from concurrent.futures import ThreadPoolExecutor

async def afunc():
    print("connect!")
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor() as executor:
        response = await loop.run_in_executor(executor, func)
    print("success!")
    return response
```