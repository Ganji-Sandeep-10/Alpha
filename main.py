from fastapi import FastAPI

app = FastAPI()  # create an instance of FastAPI

@app.get("/")  # define a GET endpoint at the root "/"
def main():
    return {
        "status": 200,
        "message": "hello world"
    }
