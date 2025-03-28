from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)

@app.post("/api/")
async def root():
    return {"answer": "Hello from Clean API"}