from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)

@app.get("/api/")
def root():
    return {"answer": "It works!"}