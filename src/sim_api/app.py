from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello Dev World"}


@app.get("/items")
def read_item():
    return {"Hello:Item"}