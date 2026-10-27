"""
Test Suite to test version reporting
"""
from fastapi.testclient import TestClient
from api import main

client = TestClient(main.app)

def test_version_endpoint():
    """
    Should return current api version
    """
    response = client.get("/version")
    assert response.status_code == 200, "Server failed due to internal error"
    assert response.json() == {"API Version": "v0.0.1"}, "API Version is incorrect"
