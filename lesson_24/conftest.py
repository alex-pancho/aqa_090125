import pytest
import requests
from requests.auth import HTTPBasicAuth

@pytest.fixture(scope="class")
def auth_session():
    session = requests.Session()
    url = "http://127.0.0.1:8080/auth"
    auth = HTTPBasicAuth('test_user', 'test_pass')
    response = session.post(url, auth=auth)

    assert response.status_code == 200
    access_token = response.json().get("access_token")
    assert access_token is not None

    session.headers.update({'Authorization': f'Bearer {access_token}'})
    return session