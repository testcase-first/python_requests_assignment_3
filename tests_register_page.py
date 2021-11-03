from requests.models import Response
from pages.register_page import RegisterPage


class SignUpUser:
    def __init__(self):
        self.register_page = RegisterPage()
        self.valid_dt = {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }

        self.invalid_email = {
            "email": "anyone@example.com",
            "password": "example"
        }

        self.invalid_pass = {
            "email": "sydney@fife"
        }

        self.email = {
            "email": "eve.holt@reqres.in"
        }

        self.empty_pass = {
            "email": "eve.holt@reqres.in",
            "password": ""
        }

    def test_post_valid_email_pass(self):
        # register_page = RegisterPage()
        response = self.register_page.post(data=self.valid_dt)
        print(response)

    def test_get_valid_email_pass(self):
        # register_page = RegisterPage()
        response = self.register_page.get(data=self.valid_dt)
        print(response)
    
    def test_post_invalid_email(self):
        response = self.register_page.post(data=self.invalid_email)
        print(response)
    
    def test_post_invalid_pass(self):
        response = self.register_page.post(data=self.invalid_pass)
        print(response)     

    def test_post_email_already_used(self):
        response = self.register_page.post(data=self.email)
        print(response)
    
    def test_post_empty_password(self):
        res = self.register_page.post(data=self.empty_pass)
        print(res)

if __name__ == "__main__":
    sign_up_user = SignUpUser()
    sign_up_user.test_post_valid_email_pass()
    sign_up_user.test_get_valid_email_pass()
    sign_up_user.test_post_invalid_email()
    sign_up_user.test_post_invalid_pass()
    sign_up_user.test_post_email_already_used()
    sign_up_user.test_post_empty_password()
