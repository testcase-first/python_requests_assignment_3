from pages.login_page import LoginPage


class SingInUser:
    def __init__(self):
        self.login_page = LoginPage()
        self.vaild_email_pass = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
        self.invalid_pass = {
            "email": "eve.holt@reqres.in",
            "password": "hello"
        }

        self.empty_pass = {
            "email": "eve.holt@reqres.in"
        }

        self.empty_email = {
            "email": "",
            "password": "cityslicka"
        }
    
    def test_post_vaild_email_pass(self):
        response = self.login_page.post(data=self.vaild_email_pass)
        print(response)
    
    def test_post_invalid_pass(self):
        res = self.login_page.post(data=self.invalid_pass)
        print(res)
    
    def test_post_empty_pass(self):
        res = self.login_page.post(data=self.empty_pass)
        print(res)

    def test_post_empty_email(self):
        res = self.login_page.post(data=self.empty_email)
        print(res)
    
    def test_get_valid_email_pass(self):
        res = self.login_page.get(data=self.vaild_email_pass)
        print(res)

if __name__ == "__main__":
    sign_in_user = SingInUser()
    sign_in_user.test_post_vaild_email_pass()
    sign_in_user.test_post_invalid_pass()
    sign_in_user.test_post_empty_pass()
    sign_in_user.test_post_empty_email()
    sign_in_user.test_get_valid_email_pass()
