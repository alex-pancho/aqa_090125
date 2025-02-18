import pytest
import requests
import threading
import time
from http.server import HTTPServer
from api_server import SimpleHTTPRequestHandler, run

BASE_URL = "http://127.0.0.1:8080"

@pytest.fixture(scope="module", autouse=True)
def start_server():
    server = HTTPServer(('localhost', 8080), SimpleHTTPRequestHandler)
    thread = threading.Thread(target=server.serve_forever)
    thread.daemon = True
    thread.start()
    time.sleep(1)  # Give the server a second to start
    yield
    server.shutdown()
    thread.join()

def test_get_content():
    response = requests.get(f"{BASE_URL}/content")
    assert response.status_code == 200
    assert response.json() == {"content": []}

def test_create_content():
    data = {"title": "Test", "body": "Test body"}
    response = requests.post(f"{BASE_URL}/content", json=data)
    assert response.status_code == 201
    assert response.json() == {"message": "Content created successfully!"}

    # Verify the content was added
    response = requests.get(f"{BASE_URL}/content")
    assert response.status_code == 200
    assert response.json() == {"content": [data]}

def test_update_content():
    data = {"title": "Updated", "body": "Updated body"}
    response = requests.put(f"{BASE_URL}/content/0", json=data)
    assert response.status_code == 200
    assert response.json() == {"message": "Content updated successfully!"}

    # Verify the content was updated
    response = requests.get(f"{BASE_URL}/content")
    assert response.status_code == 200
    assert response.json() == {"content": [data]}

def test_delete_content():
    response = requests.delete(f"{BASE_URL}/content/0")
    assert response.status_code == 200
    assert response.json() == {"message": "Content deleted successfully!"}

    # Verify the content was deleted
    response = requests.get(f"{BASE_URL}/content")
    assert response.status_code == 200
    assert response.json() == {"content": []}