import requests
from requests.exceptions import HTTPError


def get_method(url:str = "https://www.example.com", params:dict={}):
    """ Getting data... """
    response = requests.get(url, params=params)
    return response


def post_method(url:str = "https://www.example.com", data_to_send:dict = {}):
    """ Getting data... """
    response = requests.post(url, json=data_to_send)
    return response


def put_method(url:str = "https://www.example.com", data_to_send:dict = {}):
    """ Getting data... """
    response = requests.put(url, json=data_to_send)
    return response


def get_jsonplaceholder():
    url = "https://jsonplaceholder.typicode.com/comments"
    params = {'postId': 1, 'email': 'Nikita@garfield.biz'}
    res = get_method(url, params=params)
    print(res.status_code)
    try:
        print(res.json())
    except requests.exceptions.JSONDecodeError:
        print(res.text)


def post_jsonplaceholder():
    url = 'http://jsonplaceholder.typicode.com/posts'
    data_to_send = {
        'userId': 1,
        'title': 'Some title',
        'email': "Sincere@april.biz"
    }
    res = post_method(url, data_to_send)
    print(res.status_code)
    print(res.text)
    print(res.json())


def put_jsonplaceholder():
    url = 'http://jsonplaceholder.typicode.com/posts/1'
    data_to_send = {
        'userId': 1,
        'title': 'New title',
    }
    res = put_method(url, data_to_send)
    print(res.status_code)
    print(res.text)
    print(res.json())


def use_session():
    # Створення сесії
    session = requests.Session()

    # Встановлення cookies для сесії
    cookies = {'user_id': '12345', 'session_id': 'abcdef'}
    session.cookies.update(cookies)
    headers= {"Authorization": "Bearer: kldjusdih-jbJDGSJKGSJAG-sdr3cd-ss"}
    # Виконання запитів за допомогою сесії
    response1 = session.get('https://example.com/page1', headers=headers)
    return response1


if __name__ =="__main__":
    #get_jsonplaceholder()
    #post_jsonplaceholder()
    put_jsonplaceholder()
    use_session()
