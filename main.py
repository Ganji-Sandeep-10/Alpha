from fastapi import FastAPI

app=FastAPI()


@app.get("/")
def main():
    print("hello world")




@app.get("/main")
def hello():
    print("hello world")

