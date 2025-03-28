from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from Railway!"}

@app.post("/api/")
def get_answer():
    return {"answer": "It works!"}