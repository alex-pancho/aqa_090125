import json
import urllib.request
from unittest.mock import patch, MagicMock

BASE_URL = "http://127.0.0.1:8080"


def return_content(req:urllib.request.Request):
    response = urllib.request.urlopen(req)
    read_response = response.read()
    json_response = json.loads(read_response)
    return json_response


def get_content():
    req = urllib.request.Request(
        f"{BASE_URL}/content",
        headers={"Content-Type": "application/json"}
    )
    json_response = return_content(req)
    return json_response


def create_content():
    data = json.dumps(
        {"title": "Test", "body": "Test body"}
    ).encode("utf-8")
    req = urllib.request.Request(
        f"{BASE_URL}/content",
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    return return_content(req)


def update_content():
    data = json.dumps(
        {"title": "Updated", "body": "Updated body"}
    ).encode("utf-8")
    req = urllib.request.Request(
        f"{BASE_URL}/content/0",
        data=data,
        headers={"Content-Type": "application/json"},
        method="PUT",
    )
    return return_content(req)


def delete_content():
    req = urllib.request.Request(
        f"{BASE_URL}/content/0", 
        method="DELETE")
    return return_content(req)


# Mocking API requests
@patch("api_real_and_mock.get_content")
def mock_get_content(get_urlopen):
    get_urlopen.return_value = json.dumps(
        {"content": []}
    ).encode("utf-8")
    return get_urlopen()


@patch("api_real_and_mock.create_content")
def mock_create_content(create_urlopen):
    create_urlopen.return_value = json.dumps(
        {"message": "Content created successfully!"}
    ).encode("utf-8")
    return create_urlopen()


@patch("api_real_and_mock.update_content")
def mock_update_content(update_urlopen):
    update_urlopen.return_value = json.dumps(
        {"message": "Content updated successfully!"}
    ).encode("utf-8")
    return update_urlopen()


@patch("api_real_and_mock.delete_content")
def mock_delete_content(delete_urlopen):
    delete_urlopen.return_value= json.dumps(
        {"message": "Content deleted successfully!"}
    ).encode("utf-8")
    return delete_urlopen()


if __name__ == "__main__":
    print(create_content())
    print(get_content())
    print(delete_content())
    print(get_content())
    print(mock_get_content())
    print(mock_create_content())
    print(mock_update_content())
    print(mock_delete_content())
