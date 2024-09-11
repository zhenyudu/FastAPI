from fastapi import FastAPI, Request
import time

from log import logger

app = FastAPI()

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    request.state.start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - request.state.start_time
    logger.info("Client: {}:{}  - {} {} - {}".format(request.client.host, request.client.port, request.client.method, request.scope['path'], response.status_code))
    response.headers["X-Process-Time"] = str(process_time)
    return response