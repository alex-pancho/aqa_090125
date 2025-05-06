import pytest
import requests
import logging
from requests.auth import HTTPBasicAuth

# Налаштування логування
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('test_search.log', mode='w')

console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Fixture

@pytest.fixture(scope="class")
def auth_session(request):
    base_url = "http://127.0.0.1:8080/"
    session = requests.Session()
    auth = HTTPBasicAuth('test_user', 'test_pass')
    response = session.post(f"{base_url}/auth", auth=auth)

    assert response.status_code == 200, "Auth failed"
    token = response.json().get("access_token")
    assert token, "No token in response"

    session.headers.update({"Authorization": f"Bearer {token}"})
    request.cls.session = session
    request.cls.base_url = base_url

@pytest.mark.usefixtures("auth_session")
class TestCarSearch:

    @pytest.mark.parametrize("sort_by,limit", [
        ("price", 5),
        ("year", 3),
        ("engine_volume", 10),
        ("brand", 2),
        ("price", 7),
        (None, 4),
        ("year", None),
    ])

    def test_cars_endpoint(self, sort_by, limit):
        params = {}
        if sort_by:
            params["sort_by"] = sort_by
        if limit:
            params["limit"] = limit

        logger.info(f"Request to /cars with parameters: {params}")
        response = self.session.get(f"{self.base_url}/cars", params=params)

        logger.info(f"Response status code: {response.status_code}")
        logger.info(f"Response body: {response.text}")

        assert response.status_code == 200
        result = response.json()
        assert isinstance(result, list)
        if limit:
            assert len(result) <= limit