from hillel_api import API as api
import requests
import pytest


s = requests.Session()


def after_processsing(r: requests.Response):
    try:
        return r.json()
    except requests.JSONDecodeError as e:
        print(e)
        return {"nonjson": r.text}


def test_sigin_positive(get_regisered_user):
    email, password = get_regisered_user
    user_data = {
    "email": email,
    "password": password,
    "remember": False
    }
    r = api.auth.signin(s, user_data)
    r_json = after_processsing(r)    
    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not ok"


def test_sigin_negative():

    user_data_negative = {
    "email": "qam@2022test.com",
    "password": "Qam2",
    "remember": False
    }
    r = api.auth.signin(s, user_data_negative)
    r_json = after_processsing(r)
    assert r.status_code == 400, "Wrong status code"
    assert r_json["status"] == "error", "Key 'status' is not error"


def test_logout():

    r = api.auth.logout(s)
    r_json = after_processsing(r)    
    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not ok"


def test_sigin_delete_and_cant_resign(get_regisered_user):
    """E2E test example"""
    # Створення даних користувача для тестування
    email, password = get_regisered_user
    user_data = {
        "email": email,
        "password": password,
        "remember": False
    }

    # Автентифікація користувача
    r = api.auth.signin(s, user_data)
    r_json = r.json()
    
    # Перевірка успішності автентифікації
    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not ok"

    # Видалення користувача
    r = api.users.users(s)
    r_json = r.json()
    
    # Перевірка успішності видалення користувача
    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not ok"

    # Спроба повторного входу після видалення користувача (має бути помилка)
    r = api.auth.signin(s, user_data)
    r_json = r.json()
    
    # Перевірка невдалої спроби входу після видалення користувача
    assert r.status_code == 400, "Wrong status code"
    assert r_json["status"] == "error", "Key 'error' expected"
