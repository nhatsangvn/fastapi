from fastapi import FastAPI
import asyncio
import uvicorn
import time

app = FastAPI()

@app.get("/hi")
async def greet():
    await asyncio.sleep(1)
    return "Hello? World?"

@app.get("/ho")
def greet():
    time.sleep(1)
    return "Hello? World?"

if __name__ == "__main__":
    uvicorn.run("greet_async_uvicorn:app")
    print("a")