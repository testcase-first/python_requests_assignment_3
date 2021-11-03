import requests

from .base_page import BasePage


class LoginPage(BasePage):
    def __init__(self) -> None:
        super().__init__()
    
    def get(self, url="https://reqres.in/api/login", data={}):
        self.response = requests.get(url, data)
        return self.response.status_code

    def post(self, url="https://reqres.in/api/login", data={}):
        self.response = requests.post(url, data)
        return self.response.status_code, self.response.text
