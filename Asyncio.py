from fastapi import FastAPI
import time
import asyncio


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