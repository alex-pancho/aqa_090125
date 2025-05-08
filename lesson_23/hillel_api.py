import requests
base_api_url = "https://qauto.forstudy.space/api"


class Auth():

    @staticmethod
    def logout(s: requests.session, request_body: dict = {}):
        endpoint = "/auth/logout"
        return s.get(base_api_url+endpoint)

    @staticmethod
    def signup(s: requests.session, request_body: dict):
        endpoint = "/auth/signup"
        return s.post(base_api_url+endpoint, json=request_body)

    @staticmethod
    def signin(s: requests.session, request_body: dict):
        endpoint = "/auth/signin"
        return s.post(base_api_url+endpoint, json=request_body)

    @staticmethod
    def resetpassword(s: requests.session, request_body: dict):
        endpoint = "/auth/resetpassword"
        return s.post(base_api_url+endpoint, json=request_body)


class Users():

    @staticmethod
    def current(s: requests.session, request_body: dict = {}):
        endpoint = "/users/current"
        return s.get(base_api_url+endpoint)

    @staticmethod
    def profile_get(s: requests.session, request_body: dict = {}):
        endpoint = "/users/profile"
        return s.get(base_api_url+endpoint)

    @staticmethod
    def profile_put(s: requests.session, request_body: dict):
        endpoint = "/users/profile"
        return s.put(base_api_url+endpoint, json=request_body)

    @staticmethod
    def settings_get(s: requests.session, request_body: dict = {}):
        endpoint = "/users/settings"
        return s.get(base_api_url+endpoint)

    @staticmethod
    def settings_put(s: requests.session, request_body: dict):
        endpoint = "/users/settings"
        return s.put(base_api_url+endpoint, json=request_body)

    @staticmethod
    def resetpassword(s:requests.session, user_id:int, token:str):
        # TODO: make this part better
        endpoint = f"/users/resetpassword/{user_id}/{token}"
        return s.get(base_api_url+endpoint)

    @staticmethod
    def email(s: requests.session, request_body: dict):
        endpoint = "/users/email"
        return s.put(base_api_url+endpoint, json=request_body)

    @staticmethod
    def password(s: requests.session, request_body: dict):
        endpoint = "/users/password"
        return s.put(base_api_url+endpoint, json=request_body)

    @staticmethod
    def users(s: requests.session, request_body: dict = {}):
        endpoint = "/users"
        return s.delete(base_api_url+endpoint)


class Cars():
    @staticmethod
    def brands(s: requests.session, request_body: dict = {}):
        endpoint = "/cars/brands"
        return s.get(base_api_url+endpoint)

    @staticmethod
    def brands_id(s: requests.session, request_body: dict):
        id_ = request_body.get("id", 0)
        endpoint = f"/cars/brands/{id_}"
        return s.get(base_api_url+endpoint)

    @staticmethod
    def models(s: requests.session, request_body: dict = {}):
        endpoint = "/cars/models"
        return s.get(base_api_url+endpoint)

    @staticmethod
    def models_id(s: requests.session, request_body: dict):
        id_ = request_body.get("id", 0)
        endpoint = f"/cars/models/{id_}"
        return s.get(base_api_url+endpoint)

    @staticmethod
    def cars_get(s: requests.session, request_body: dict = {}):
        endpoint = "/cars"
        return s.get(base_api_url+endpoint)

    @staticmethod
    def cars_post(s: requests.session, request_body: dict):
        endpoint = "/cars"
        return s.post(base_api_url+endpoint, json=request_body)

    @staticmethod
    def cars_id_get(s: requests.session, request_body: dict):
        id_ = request_body.get("id", 0)
        endpoint = f"/cars/{id_}"
        return s.get(base_api_url+endpoint)

    @staticmethod
    def cars_id_put(s: requests.session, request_body: dict):
        id_ = request_body.pop("id", 0)
        endpoint = f"/cars/{id_}"
        return s.put(base_api_url+endpoint, json=request_body)

    @staticmethod
    def cars_id_delete(s: requests.session, request_body: dict):
        id_ = request_body.get("id", 0)
        endpoint = f"/cars/{id_}"
        return s.delete(base_api_url+endpoint)


class Expenses():

    @staticmethod
    def expenses_get(s: requests.session, request_body: dict):
        car_id = request_body.get("id", 0)
        page = request_body.get("page", 0)
        endpoint = "/expenses"
        query = {"carId": car_id, "page": page}
        return s.get(base_api_url+endpoint, params=query)

    @staticmethod
    def expenses_post(s: requests.session, request_body: dict):
        endpoint = "/expenses"
        return s.post(base_api_url+endpoint, json=request_body)

    @staticmethod
    def expenses_id_get(s: requests.session, request_body: dict):
        id_ = request_body.get("id", 1)
        endpoint = f"/expenses/{id_}"
        return s.get(base_api_url+endpoint)

    @staticmethod
    def expenses_id_put(s: requests.session, request_body: dict):
        id_ = request_body.pop("id") if request_body.get("id") is not None else request_body.get("carId", 1)
        endpoint = f"/expenses/{id_}"
        return s.put(base_api_url+endpoint, json=request_body)

    @staticmethod
    def expenses_id_delete(s: requests.session, request_body: dict):
        id_ = request_body.get("id", 1)
        endpoint = f"/expenses/{id_}"
        return s.delete(base_api_url+endpoint)


class Instructions():

    @staticmethod
    def instructions(s: requests.session, request_body: dict):
        car_brand_id = request_body.get("carBrandId", 0)
        car_model_id = request_body.get("carModelId", 0)
        page = request_body.get("page", 0)
        endpoint = "/instructions"
        query = {"carBrandId": car_brand_id,
                 "carModelId": car_model_id,
                 "page": page}
        return s.get(base_api_url+endpoint, params=query)

    @staticmethod
    def instructions_id(s: requests.session, request_body: dict):
        id_ = request_body.get("id", 1)
        endpoint = f"/instructions/{id_}"
        return s.get(base_api_url+endpoint)


class API():
    auth = Auth()
    users = Users()
    cars = Cars()
    expenses = Expenses()
    instructions = Instructions()

