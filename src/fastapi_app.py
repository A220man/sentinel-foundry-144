from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
async def hello():
    return {"message": "Hello, world!"}


@app.get("/health")
async def health():
    return {"status": "healthy", "service": "sentinel-foundry-144"}
