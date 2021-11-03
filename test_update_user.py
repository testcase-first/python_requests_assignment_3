import requests
import json

class UpdateUser:
    def __init__(self, url) -> None:
        self.url = url
        self.valid_data = {
            "name": "morpheus",
            "job": "zion resident"
        }

    def test_post_update_user(self):
        res = requests.post(self.url, data=self.valid_data)
        res_dict = json.loads(res.text)
        res_string_indent = json.dumps(res_dict, indent=2)
        print(res_string_indent)


if __name__ == "__main__":
    update_user = UpdateUser("https://reqres.in/api/users/2")
    update_user.test_post_update_user()