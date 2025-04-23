import pytest
import requests

from requests.auth import HTTPBasicAuth
from lesson_24.logger import logger

BASE_URL = "http://127.0.0.1:8080"
USERNAME = "test_user"
PASSWORD = "test_pass"


class HttpCarsClient:
    def __init__(self):
        self.rs = requests.Session()

    def auth_signin(self):
        auth_endpoint = "/auth"
        res = self.rs.post(BASE_URL + auth_endpoint, auth=HTTPBasicAuth(USERNAME, PASSWORD))
        logger.debug(f"Status code: {res.status_code}, JSON data: {res.json()}")
        access_token = res.json().get("access_token", False)
        if not access_token:
            logger.error("Access token is missing")
            pytest.fail("Access token is missing")
        self.update_header(access_token)
        return res

    def update_header(self, access_token: str):
        self.rs.headers.update({'Authorization': 'Bearer ' + access_token})
        return self

    def get_cars(self, params: dict):
        get_cars_endpoint = "/cars"
        logger.info(f"URL: {BASE_URL}{get_cars_endpoint}, Params: {params}")
        res = self.rs.get(BASE_URL + get_cars_endpoint, params=params)
        logger.debug(f"Status code: {res.status_code}, JSON data: {res.json()}")
        return res
