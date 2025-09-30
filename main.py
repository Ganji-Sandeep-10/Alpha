from fastapi import FastAPI

app=FastAPI()


@app.get("/")
def main():
    print("hello world")