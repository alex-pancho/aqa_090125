import pytest
from hillel_api import API
import requests

@pytest.fixture
def get_regisered_user():
    email = "alex22222@gmail.com"
    password = "AA12aa!@"
    query_data = {
        "name": "name",
        "lastName": "lastname",
        "email": email,
        "password": password,
        "repeatPassword": password
    }
    s = requests.Session()
    r = API.auth.signup(s, request_body=query_data)
    if r.status_code != 201:
        raise AttributeError(r.text)
    yield email, password
    API.users.users(s)

