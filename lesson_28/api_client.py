import requests

BASE_URL = "https://qauto2.forstudy.space/api"

class ApiClient:
    def __init__(self):
        self.session = requests.Session()

    def login(self, email, password, remember=False):
        """Логін користувача через API."""
        url = f"{BASE_URL}/auth/signin"
        response = self.session.post(url, json={
            "email": email,
            "password": password,
            "remember": remember
        })
        response.raise_for_status()

    def delete_user(self):
        """Видалення користувача через API."""
        url = f"{BASE_URL}/users"
        response = self.session.delete(url)
        response.raise_for_status()
