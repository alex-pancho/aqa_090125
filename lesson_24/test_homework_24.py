import pytest
from logger import logger


PRICE_LIMIT_3_DATA = [
    {'brand': 'Chevrolet', 'engine_volume': 1.8, 'price': 28000, 'year': 2018},
    {'brand': 'Hyundai', 'engine_volume': 1.6, 'price': 29000, 'year': 2020},
    {'brand': 'Honda', 'engine_volume': 1.6, 'price': 30000, 'year': 2016}
]

BRAND_LIMIT_4_DATA = [
    {'brand': 'Acura', 'year': 2020, 'engine_volume': 2.4, 'price': 48000},
    {'brand': 'Audi', 'year': 2020, 'engine_volume': 1.8, 'price': 45000},
    {'brand': 'BMW', 'year': 2018, 'engine_volume': 2.0, 'price': 50000},
    {'brand': 'Bugatti', 'year': 2019, 'engine_volume': 8.0, 'price': 350000}
]

YEAR_LIMIT_5_DATA = [
    {'brand': 'Ford', 'engine_volume': 2.2, 'price': 32000, 'year': 2015},
    {'brand': 'Honda', 'engine_volume': 1.6, 'price': 30000, 'year': 2016},
    {'brand': 'Toyota', 'engine_volume': 2.4, 'price': 35000, 'year': 2017},
    {'brand': 'Subaru', 'engine_volume': 2.5, 'price': 40000, 'year': 2017},
    {'brand': 'BMW', 'engine_volume': 2.0, 'price': 50000, 'year': 2018}
]

ENGINE_VOLUME_LIMIT_2 = [
    {'brand': 'Tesla', 'year': 2020, 'engine_volume': 0.0, 'price': 80000},
    {'brand': 'Nissan', 'year': 2021, 'engine_volume': 1.5, 'price': 40000}
]

NO_SORT_LIMIT_3 = [
    {'brand': 'Acura', 'year': 2020, 'engine_volume': 2.4, 'price': 48000},
    {'brand': 'Audi', 'year': 2020, 'engine_volume': 1.8, 'price': 45000},
    {'brand': 'BMW', 'year': 2018, 'engine_volume': 2.0, 'price': 50000}
]


test_cases = [
    ("price", 3, PRICE_LIMIT_3_DATA),
    ("brand", 4, BRAND_LIMIT_4_DATA),
    ("year", 5, YEAR_LIMIT_5_DATA),
    ("engine_volume", 2, ENGINE_VOLUME_LIMIT_2),
    (None, 3, NO_SORT_LIMIT_3)
]

class TestCarSearch:

    @pytest.mark.parametrize("sort_by, limit, expected", test_cases)
    def test_search_cars_expected(self, auth_session, sort_by, limit, expected):
        logger.info(f"Testing with sort_by={sort_by}, limit={limit}")
        params = {}
        if sort_by:
            params["sort_by"] = sort_by
        if limit:
            params["limit"] = limit

        response = auth_session.get("http://127.0.0.1:8080/cars", params=params)

        logger.debug(f"Status Code: {response.status_code}")
        logger.debug(f"Response JSON: {response.json()}")

        assert response.status_code == 200
        actual = response.json()

        assert actual == expected