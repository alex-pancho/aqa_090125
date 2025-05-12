import pytest
import requests
import logging
from requests.auth import HTTPBasicAuth

# Логування для тестів
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
logger.addHandler(logging.StreamHandler())
logger.addHandler(logging.FileHandler('test_search.log', mode='w'))

@pytest.fixture(scope="class")
def auth_session(request):
    base_url = "http://127.0.0.1:8080"
    session = requests.Session()
    auth = HTTPBasicAuth('test_user', 'test_pass')

    response = session.post(f"{base_url}/auth", auth=auth)
    assert response.status_code == 200, "Auth failed"
    token = response.json().get("access_token")
    assert token, "Token missing"

    session.headers.update({"Authorization": f"Bearer {token}"})
    request.cls.session = session
    request.cls.base_url = base_url

@pytest.mark.usefixtures("auth_session")
class TestCarSearch:

    @pytest.mark.parametrize("sort_by,limit", [
        ("price", 3),
        ("year", 2),
        ("engine_volume", 5),
        ("brand", 1),
        (None, 4),
        ("year", None),
        ("not_a_field", 2),  # negative test
        ("year", "invalid"), # negative test
    ])
    def test_cars_endpoint(self, sort_by, limit):
        params = {}
        if sort_by:
            params["sort_by"] = sort_by
        if limit:
            params["limit"] = limit

        logger.info(f"Testing /cars with params: {params}")
        response = self.session.get(f"{self.base_url}/cars", params=params)
        logger.info(f"Status: {response.status_code}, Body: {response.text}")

        if sort_by in ["not_a_field"]:
            assert response.status_code == 400
            return
        if limit == "invalid":
            assert response.status_code == 400
            return

        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        if limit:
            try:
                expected = int(limit)
                assert len(data) <= expected
            except ValueError:
                pass
