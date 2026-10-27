"""
Test Suite to test api root
"""
from fastapi.testclient import TestClient
from api import main

client = TestClient(main.app)

def test_root_endpoint():
    """
    Should return Hello World!
    """
    response = client.get("/")
    assert response.status_code == 200, "Server failed due to internal error"
    assert response.json() == {"Body": "Hello World!"}, "Root endpoint not returning Hello World!"
