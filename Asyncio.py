from fastapi import FastAPI
import time
import asyncio
from concurrent.futures import ProcessPoolExecutor
from functools import partial


N = 100000000

async def acal(a, b):
    start = time.time()
    for x in range(N):
        a += x
        a -= x
    end = time.time() - start
    return a+b, end

def cal(a, b):
    start = time.time()
    for x in range(N):
        a += x
        a -= x
    end = time.time() - start
    return a+b, end

app = FastAPI()

#同步函數同步方法
@app.get("/root/1/")
def root1():
    print("connect!")
    time.sleep(3)
    print("success!")
    return {"response": "200"}

#異步函數同步方法
@app.get("/root/2/")
async def root2():
    print("connect!")
    time.sleep(3)
    print("success!")
    return {"response": "200"}

#異步函數異步方法
@app.get("/root/3/")
async def root3():
    print("connect!")
    await asyncio.sleep(3)
    print("success!")
    return {"response": "200"}

#異步函數線程執行run_in_executor
@app.get("/root/4/")
async def root4():
    print("connect!")
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, time.sleep, 3)
    print("success!")
    return {"response": "200"}


@app.get("/cal/1")
async def func1():
    print("connect!")
    n, end = await acal(10, 8)
    print("success!")
    return {'value': n, 'time': end}

# loop = asyncio.get_event_loop()
# process_pool = ProcessPoolExecutor()

#CPU型任務需要套用ProcessPoolExecutor()來開啟多線程
@app.get("/cal/2")
async def func1():
    print("connect!")
    n, end = await loop.run_in_executor(process_pool, partial(cal, 10, 8))
    print("success!")
    return {'value': n, 'time': end}



# 在應用啟動時觸發
@app.on_event("startup")
async def startup_event():
    global process_pool, loop
    loop = asyncio.get_event_loop()
    process_pool = ProcessPoolExecutor()

# 在應用關閉時觸發
@app.on_event("shutdown")
async def shutdown_event():
    global process_pool
    process_pool.shutdown()