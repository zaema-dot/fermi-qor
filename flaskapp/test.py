import requests
import pytest
import os

# Base URL of your Flask API
# BASE_URL = "http://172.18.0.3:5000"
BASE_URL = os.getenv("BASE_URL", "https://9ac2-203-99-184-187.ngrok-free.app")
#BASE_URL = os.getenv("NGROK_URL", "http://172.18.0.3:5000")


# Test data for different queries
test_data = [
    {"query_type": "job_id", "query_value": "917", "stats_type": "main"},
    {"query_type": "job_id", "query_value": "917", "stats_type": "all"},
    {"query_type": "job_id", "query_value": "917", "stats_type": "runtime"},
    {"query_type": "job_id", "query_value": "917", "stats_type": "statistical"},
    {"query_type": "job_id", "query_value": "917", "stats_type": "geometric"},
    {"query_type": "user_id", "query_value": "exampleuser", "stats_type": "main"},
    {"query_type": "user_id", "query_value": "exampleuser", "stats_type": "all"},
    {"query_type": "user_id", "query_value": "exampleuser", "stats_type": "runtime"},
    {"query_type": "user_id", "query_value": "exampleuser", "stats_type": "statistical"},
    {"query_type": "user_id", "query_value": "exampleuser", "stats_type": "geometric"},
    {"query_type": "job_name", "query_value": "exampleDesign01", "stats_type": "main"},
    {"query_type": "job_name", "query_value": "exampleDesign01", "stats_type": "all"},
    {"query_type": "job_name", "query_value": "exampleDesign01", "stats_type": "runtime"},
    {"query_type": "job_name", "query_value": "exampleDesign01", "stats_type": "statistical"},
    {"query_type": "job_name", "query_value": "exampleDesign01", "stats_type": "geometric"}
]

invalid_test_data = [
    {"query_type": "job_id", "query_value": "99999", "stats_type": "main"},
    {"query_type": "job_id", "query_value": "invalid_id", "stats_type": "all"},
    {"query_type": "user_id", "query_value": "nonexistentuser", "stats_type": "main"},
    {"query_type": "job_name", "query_value": "invalidJobName", "stats_type": "main"}
]

# Test 1: Check if the home page loads with status code 200 and response time < 200ms
def test_homepage_loading():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 2  # Response time less than 200ms

# Test 2: Combination tests for different query types and stats types
@pytest.mark.parametrize("data", test_data)
def test_query_combinations(data):
    response = requests.post(
        f"{BASE_URL}/",
        data={
            "query_type": data["query_type"],
            "query_value": data["query_value"],
            "stats_type": data["stats_type"]
        }
    )
    assert response.status_code == 200

   # Check based on stats_type
    if data["stats_type"] == "main":
        assert "Main Stats" in response.text
    elif data["stats_type"] == "runtime":
        assert "Runtime Analysis" in response.text
    elif data["stats_type"] == "statistical":
        assert "Statistical Analysis" in response.text
    elif data["stats_type"] == "geometric":
        assert "Geometric Analysis" in response.text
    elif data["stats_type"] == "all":
        assert "Main Stats" in response.text
        assert "Runtime Analysis" in response.text
        assert "Statistical Analysis" in response.text
        assert "Geometric Analysis" in response.text

# Test 3: Combination tests for invalid queries that should return 404 status code
@pytest.mark.parametrize("data", invalid_test_data)
def test_invalid_query_combinations(data):
    response = requests.post(
        f"{BASE_URL}/",
        data={
            "query_type": data["query_type"],
            "query_value": data["query_value"],
            "stats_type": data["stats_type"]
        }
    )
    assert response.status_code == 404