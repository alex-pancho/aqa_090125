import requests
import pytest
import logging
from requests.auth import HTTPBasicAuth
from logging_config import setup_logging 


setup_logging()

AUTH_URL = "http://127.0.0.1:8080/auth"
AUTH_DATA = HTTPBasicAuth('test_user', 'test_pass')
session = requests.Session()

@pytest.fixture(scope="class")
def auth_token(): 
    response = session.post(AUTH_URL, auth=AUTH_DATA)
    assert response.status_code == 200, "Authentication error"  
    
    token = response.json()['access_token'] 
    assert token, "Token not found in response"

    session.headers.update({'Authorization': 'Bearer ' + token})  
    return session

@pytest.mark.parametrize("sort_by, limit, expected_brands", [
    ("price", 5, ["Chevrolet", "Hyundai", "Honda", "Kia", "Ford"]),
    ("year", 3, ["Ford", "Honda", "Toyota"]),
    ("engine_volume", 4, ["Tesla", "Nissan", "Honda", "Hyundai"])
])

def test_search_cars(auth_token, sort_by, limit, expected_brands):
    logging.info(f"Starting test with sort_by={sort_by} and limit={limit}")  
    url = f"http://127.0.0.1:8080/cars?sort_by={sort_by}&limit={limit}"  
    response = auth_token.get(url) 
    assert response.status_code == 200
    
    cars = response.json() 
    logging.info(f"Received cars: {cars}")
    assert len(cars) == limit
    
    actual_brands = [car["brand"] for car in cars]
    logging.info(f"Actual brands in response: {actual_brands}")
    assert actual_brands == expected_brands