"""
Test Suite to test average temperature
"""
from fastapi.testclient import TestClient
from api import main

client = TestClient(main.app)

def test_temperature_endpoint():
    """
    Should return average temperature
    """
    response = client.get("/temperature")
    data = response.json()
    assert response.status_code == 200, "Server failed due to internal error"
    assert "Average Temperature" in data, "Key 'Average Temperature' not found in Response"

def test_temperature_valid():
    """
    Should return average temperature between -30C and 50C
    """
    response = client.get("/temperature")
    assert response.status_code == 200, "Server failed due to internal error"
    data = response.json()
    avg_temp = data["Average Temperature"]
    assert -30 < float(avg_temp) < 50, "Average Temperature is invalid"

def test_temperature_status():
    """
    Should return temperature status(Too Cold/Good/Too Hot) based on average temperature
    """
    response = client.get("/temperature")
    assert response.status_code == 200, "Server failed due to internal error"
    data = response.json()
    status = data["Status"]
    assert status in ["Too Cold", "Good", "Too Hot"], "Temperature Status is invalid"

def test_temperature_good(monkeypatch):
    """
    Should return temperature status as Good based on average temperature between 11 and 36
    """
    monkeypatch.setattr(main.requests, "get", lambda *args, **kwargs: MockGoodResponse())
    response = client.get("/temperature")
    assert response.status_code == 200, "Server failed due to internal error"
    data = response.json()
    avg_temp = data["Average Temperature"]
    status = data["Status"]
    assert status == "Good", ("Temperature status should be Good if avg temp between 11 and 36 "
                                  f"but avg temp is {avg_temp} and status is {status}")

def test_temperature_too_cold(monkeypatch):
    """
    Should return temperature status as Too Cold based on average temperature <= 10
    """
    monkeypatch.setattr(main.requests, "get", lambda *args, **kwargs: MockTooColdResponse())
    response = client.get("/temperature")
    assert response.status_code == 200, "Server failed due to internal error"
    data = response.json()
    avg_temp = data["Average Temperature"]
    status = data["Status"]
    assert status == "Too Cold", ("Temperature status should be Too Cold if avg temp <= 10 "
                                  f"but avg temp is {avg_temp} and status is {status}")


def test_temperature_too_hot(monkeypatch):
    """
    Should return temperature status as Too Hot based on average temperature >= 37
    """
    monkeypatch.setattr(main.requests, "get", lambda *args, **kwargs: MockTooHotResponse())

    response = client.get("/temperature")
    assert response.status_code == 200, "Server failed due to internal error"
    data = response.json()
    avg_temp = data["Average Temperature"]
    status = data["Status"]
    assert status == "Too Hot", ("Temperature status should be Too Hot if avg temp >= 37 "
                                  f"but avg temp is {avg_temp} and status is {status}")

class MockGoodResponse():
    """Mock response for test case: test_temperature_good"""
    status_code = 200
    def json(self):
        """Returns mock json response"""
        return {
            "sensors": [
                {"lastMeasurement": {"value": "32.0"}}
            ]
        }

class MockTooHotResponse():
    """Mock response for test case: test_temperature_too_hot"""
    status_code = 200
    def json(self):
        """Returns mock json response"""
        return {
            "sensors": [
                {"lastMeasurement": {"value": "40.0"}}
            ]
        }

class MockTooColdResponse():
    """Mock response for test case: test_temperature_too_cold"""
    status_code = 200
    def json(self):
        """Returns mock json response"""
        return {
            "sensors": [
                {"lastMeasurement": {"value": "8.0"}}
            ]
        }
