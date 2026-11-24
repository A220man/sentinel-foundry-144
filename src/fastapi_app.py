from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
async def hello():
    return {"message": "Hello, world!"}


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/status")
async def status():
    return {"version": "1.1.0"}
