import pytest


PRICE_SORT_LIMIT_4_DATA = [
    {'brand': 'Chevrolet', 'engine_volume': 1.8, 'price': 28000, 'year': 2018},
    {'brand': 'Hyundai', 'engine_volume': 1.6, 'price': 29000, 'year': 2020},
    {'brand': 'Honda', 'engine_volume': 1.6, 'price': 30000, 'year': 2016},
    {'brand': 'Kia', 'engine_volume': 2.0, 'price': 31000, 'year': 2019}
]

BRAND_SORT_LIMIT_3_DATA = [
    {'brand': 'Acura', 'engine_volume': 2.4, 'price': 48000, 'year': 2020},
    {'brand': 'Audi', 'engine_volume': 1.8, 'price': 45000, 'year': 2020},
    {'brand': 'BMW', 'engine_volume': 2.0, 'price': 50000, 'year': 2018}
]

YEAR_SORT_LIMIT_5_DATA = [
    {'brand': 'Ford', 'engine_volume': 2.2, 'price': 32000, 'year': 2015},
    {'brand': 'Honda', 'engine_volume': 1.6, 'price': 30000, 'year': 2016},
    {'brand': 'Toyota', 'engine_volume': 2.4, 'price': 35000, 'year': 2017},
    {'brand': 'Subaru', 'engine_volume': 2.5, 'price': 40000, 'year': 2017},
    {'brand': 'BMW', 'engine_volume': 2.0, 'price': 50000, 'year': 2018}
]

ENGINE_VOLUME_LIMIT_6_DATA = [
    {'brand': 'Tesla', 'engine_volume': 0.0, 'price': 80000, 'year': 2020},
    {'brand': 'Nissan', 'engine_volume': 1.5, 'price': 40000, 'year': 2021},
    {'brand': 'Honda', 'engine_volume': 1.6, 'price': 30000, 'year': 2016},
    {'brand': 'Hyundai', 'engine_volume': 1.6, 'price': 29000, 'year': 2020},
    {'brand': 'Audi', 'engine_volume': 1.8, 'price': 45000, 'year': 2020},
    {'brand': 'Chevrolet', 'engine_volume': 1.8, 'price': 28000, 'year': 2018}
]

PRICE_SORT_DATA = [
    {'brand': 'Chevrolet', 'engine_volume': 1.8, 'price': 28000, 'year': 2018},
    {'brand': 'Hyundai', 'engine_volume': 1.6, 'price': 29000, 'year': 2020},
    {'brand': 'Honda', 'engine_volume': 1.6, 'price': 30000, 'year': 2016},
    {'brand': 'Kia', 'engine_volume': 2.0, 'price': 31000, 'year': 2019},
    {'brand': 'Ford', 'engine_volume': 2.2, 'price': 32000, 'year': 2015},
    {'brand': 'Mazda', 'engine_volume': 2.0, 'price': 32000, 'year': 2018}
    , {'brand': 'Volkswagen', 'engine_volume': 2.0, 'price': 33000, 'year': 2019},
    {'brand': 'Toyota', 'engine_volume': 2.4, 'price': 35000, 'year': 2017},
    {'brand': 'Nissan', 'engine_volume': 1.5, 'price': 40000, 'year': 2021},
    {'brand': 'Subaru', 'engine_volume': 2.5, 'price': 40000, 'year': 2017},
    {'brand': 'Audi', 'engine_volume': 1.8, 'price': 45000, 'year': 2020},
    {'brand': 'Jeep', 'engine_volume': 3.6, 'price': 45000, 'year': 2018},
    {'brand': 'Volvo', 'engine_volume': 2.0, 'price': 46000, 'year': 2019},
    {'brand': 'Acura', 'engine_volume': 2.4, 'price': 48000, 'year': 2020},
    {'brand': 'BMW', 'engine_volume': 2.0, 'price': 50000, 'year': 2018},
    {'brand': 'Infiniti', 'engine_volume': 3.5, 'price': 52000, 'year': 2019},
    {'brand': 'Mercedes', 'engine_volume': 2.5, 'price': 55000, 'year': 2019},
    {'brand': 'Land Rover', 'engine_volume': 2.0, 'price': 55000, 'year': 2020},
    {'brand': 'Lexus', 'engine_volume': 3.0, 'price': 60000, 'year': 2021},
    {'brand': 'Porsche', 'engine_volume': 3.0, 'price': 70000, 'year': 2021},
    {'brand': 'Tesla', 'engine_volume': 0.0, 'price': 80000, 'year': 2020},
    {'brand': 'Ferrari', 'engine_volume': 6.3, 'price': 250000, 'year': 2021},
    {'brand': 'McLaren', 'engine_volume': 4.0, 'price': 280000, 'year': 2021},
    {'brand': 'Lamborghini', 'engine_volume': 6.5, 'price': 300000, 'year': 2020},
    {'brand': 'Bugatti', 'engine_volume': 8.0, 'price': 350000, 'year': 2019}
]

LIMIT_ONLY_DATA = [
    {'brand': 'Acura', 'engine_volume': 2.4, 'price': 48000, 'year': 2020},
    {'brand': 'Audi', 'engine_volume': 1.8, 'price': 45000, 'year': 2020}
]


DATA = {
    "sorts_by_price_and_limit_4": [{"sort_by": "price", "limit": 4}, {"res": PRICE_SORT_LIMIT_4_DATA}],
    "sort_by_brand_and_limit_3": [{"sort_by": "brand", "limit": 3}, {"res": BRAND_SORT_LIMIT_3_DATA}],
    "sort_by_year_and_limit_5": [{"sort_by": "year", "limit": 5}, {"res": YEAR_SORT_LIMIT_5_DATA}],
    "sort_by_engine_volume_and_limit_6": [
        {"sort_by": "engine_volume", "limit": 6},
        {"res": ENGINE_VOLUME_LIMIT_6_DATA}
    ],
    "sort_by_engine_volume_and_limit_0": [{"sort_by": "engine_volume", "limit": 0}, {"res": []}],
    "sorts_by_price": [{"sort_by": "price"}, {"res": PRICE_SORT_DATA}],
    "limit_only": [{"limit": 2}, {"res": LIMIT_ONLY_DATA}],
}


class TestHomework24:

    @pytest.mark.parametrize("data", DATA.values(), ids=DATA.keys())
    def test_get_cars(self, auth_signin, data):
        res = auth_signin.get_cars(params=data[0])
        assert res.status_code == 200, "Wrong cars response status code"
        assert res.json() == data[1]["res"], "Wrong cars response json data"
