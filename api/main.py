"""HiveBox API Core"""
import requests
from fastapi import FastAPI, HTTPException
from . import __version__

app = FastAPI()


@app.get("/")
def hello_world():
    "Returns Hello World"
    return {"Body": "Hello World!"}

@app.get("/version")
def app_version():
    "Return the current app version"
    return {"API Version": __version__}

@app.get("/temperature")
def avg_temperature():
    """
    Returns the average temperature based on all sensebox data
    Future Improvements: Add parameters functionality
    """
    base_url = "https://api.opensensemap.org/boxes/"
    boxes = ["68a93536e035980007f6036b", "689fffee29cb2f00079914d8", "689ffa2829cb2f00078f774b"]
    temps = []
    for box in boxes:
        response = requests.get(base_url + box, timeout=10)
        if response.status_code == 200:
            data = response.json()
            temps.append(float(data["sensors"][0]["lastMeasurement"]["value"]))
        else:
            raise HTTPException(
                status_code=response.status_code,
                detail={"Status": response.status_code, "Body": "Internal Error"}
                )

    avg_temp = sum(temps) / len(temps)
    return {"Average Temperature": str(avg_temp)}

if __name__ == "__main__":
    print(app_version())
