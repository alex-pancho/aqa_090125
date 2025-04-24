import pytest
import logging

BASE_URL = 'http://127.0.0.1:8080'
CARS_DB = {
    1: {"brand": "BMW", "year": 2018, "engine_volume": 2.0, "price": 50000},
    2: {"brand": "Audi", "year": 2020, "engine_volume": 1.8, "price": 45000},
    3: {"brand": "Mercedes", "year": 2019, "engine_volume": 2.5, "price": 55000},
    4: {"brand": "Toyota", "year": 2017, "engine_volume": 2.4, "price": 35000},
    5: {"brand": "Honda", "year": 2016, "engine_volume": 1.6, "price": 30000},
    6: {"brand": "Nissan", "year": 2021, "engine_volume": 1.5, "price": 40000},
    7: {"brand": "Ford", "year": 2015, "engine_volume": 2.2, "price": 32000},
    8: {"brand": "Chevrolet", "year": 2018, "engine_volume": 1.8, "price": 28000},
    9: {"brand": "Volkswagen", "year": 2019, "engine_volume": 2.0, "price": 33000},
    10: {"brand": "Hyundai", "year": 2020, "engine_volume": 1.6, "price": 29000},
    11: {"brand": "Kia", "year": 2019, "engine_volume": 2.0, "price": 31000},
    12: {"brand": "Subaru", "year": 2017, "engine_volume": 2.5, "price": 40000},
    13: {"brand": "Mazda", "year": 2018, "engine_volume": 2.0, "price": 32000},
    14: {"brand": "Lexus", "year": 2021, "engine_volume": 3.0, "price": 60000},
    15: {"brand": "Infiniti", "year": 2019, "engine_volume": 3.5, "price": 52000},
    16: {"brand": "Acura", "year": 2020, "engine_volume": 2.4, "price": 48000},
    17: {"brand": "Jeep", "year": 2018, "engine_volume": 3.6, "price": 45000},
    18: {"brand": "Land Rover", "year": 2020, "engine_volume": 2.0, "price": 55000},
    19: {"brand": "Volvo", "year": 2019, "engine_volume": 2.0, "price": 46000},
    20: {"brand": "Porsche", "year": 2021, "engine_volume": 3.0, "price": 70000},
    21: {"brand": "Tesla", "year": 2020, "engine_volume": 0.0, "price": 80000},
    22: {"brand": "Ferrari", "year": 2021, "engine_volume": 6.3, "price": 250000},
    23: {"brand": "Lamborghini", "year": 2020, "engine_volume": 6.5, "price": 300000},
    24: {"brand": "Bugatti", "year": 2019, "engine_volume": 8.0, "price": 350000},
    25: {"brand": "McLaren", "year": 2021, "engine_volume": 4.0, "price": 280000},
}

class TestCarsAPI:
    @pytest.mark.parametrize(
        "sort_by, limit, expected_count, expected_first_item_key, expected_order",
        [
            (None, None, 25, 'brand', None),
            ('brand', None, 25, 'brand', 'Acura'),
            ('year', None, 25, 'year', 2015),
            ('price', None, 25, 'price', 28000),
            ('engine_volume', None, 25, 'engine_volume', 0.0),
            ('brand', 5, 5, 'brand', 'Acura'),
            ('year', 3, 3, 'year', 2015),
            ('price', 7, 7, 'price', 28000),
            ('engine_volume', 2, 2, 'engine_volume', 0.0),
            ('invalid_sort_by', None, 25, 'brand', 'BMW'),
        ]
    )
    def test_get_cars_with_parameters(self, api_session, sort_by, limit, expected_count, expected_first_item_key, expected_order):
        """Тестує ендпоінт /cars з різними параметрами сортування та ліміту."""
        logging.info(f"Testing /cars with params: sort_by={sort_by}, limit={limit}")
        params = {}
        if sort_by:
            params['sort_by'] = sort_by
        if limit:
            params['limit'] = limit

        response = api_session.get(f'{BASE_URL}/cars', params=params)
        logging.info(f"Response status code: {response.status_code}")
        assert response.status_code == 200
        cars = response.json()
        logging.info(f"{len(cars)} cars got")
        assert len(cars) == expected_count

        if cars:
            first_car = cars[0]
            assert expected_first_item_key in first_car
            if expected_order is not None:
                assert first_car.get(expected_first_item_key) == expected_order
                logging.info(f"Firs car sorted by '{expected_first_item_key}': {first_car.get(expected_first_item_key)}")
        else:
            logging.warning("Emty list")
            