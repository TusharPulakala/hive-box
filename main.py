"""Prints the current app version"""
from fastapi import FastAPI
from _version import __version__

app = FastAPI()


@app.get("/")
def hello_world():
    "Root endpoint returns Hello World"
    return {"Body": "Hello World!"}

@app.get("/version")
def app_version():
    "Return the current app version"
    return {"App Version": __version__}

@app.get("/temperature")
def avg_temperature():
    """
    Returns the average temperateure based on all sensebox data
    Improvements: Add parameters functionality
    """
    return {"Average Temperature": "Dummy Value"}

if __name__ == "__main__":
    print(app_version())
