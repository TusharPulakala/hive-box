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
