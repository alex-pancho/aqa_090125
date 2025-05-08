import requests

base_url = "https://qauto.forstudy.space/api"
rs = requests.Session()


def auth_signup(name:str, last_name:str, email:str, password:str):
    endpoint_url = "/auth/signup"
    query_data = {
        "name": name,
        "lastName": last_name,
        "email": email,
        "password": password,
        "repeatPassword": password
    }
    return rs.post(base_url+endpoint_url, json=query_data)


def auth_signin(email:str, password:str):
    endpoint_url = "/auth/signin"
    query_data = {
        "email": email,
        "password": password,
        "remember": False
    }
    return rs.post(base_url+endpoint_url, json=query_data)


def delete(email:str, password:str):
    auth_signin(email, password)
    endpoint_url = "/users"
    return rs.delete(base_url+endpoint_url)


def print_res(res: requests.Response):
    print(res.status_code)
    print(res.headers)
    print(res.json())


if __name__ == "__main__":
    email = "alex22222@gmail.com"
    password = "AA12aa!@"
    #r = auth_signup("Alexasdf", "Xelasdf", "alex22222@gmail.com", "AA12aa!@")
    # r = auth_signin(email, password)
    #r = delete(email, password)
    print_res(r)
