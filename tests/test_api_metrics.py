"""
Test Suite to test api /metrics endpoint
"""
from fastapi.testclient import TestClient
from api import main

client = TestClient(main.app)

def test_api_metrics():
    """
    Should return api metrics
    """
    response = client.get("/version")

    metrics_response = client.get("/metrics")
    assert metrics_response.status_code == 200, "Server failed due to internal error, metrics not populating"
