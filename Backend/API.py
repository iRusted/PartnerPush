from fastapi import FastAPI

app = FastAPI()

@app.get("/test")
def say_hi():
    return {"Hi!"}