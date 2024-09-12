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

#CPU型任務需要套用ProcessPoolExecutor()來開啟多線程
@app.get("/cal/2")
async def func1():
    print("connect!")
    loop = asyncio.get_event_loop()
    with ProcessPoolExecutor() as pool:
        n, end = await loop.run_in_executor(pool, partial(cal, 10, 8))
    print("success!")
    return {'value': n, 'time': end}