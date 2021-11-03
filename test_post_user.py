import requests
import json


class CreatUser:
    def __init__(self, url) -> None:
        self.url = url
        self.vaild_data = {
            "name": "morpheus",
            "job": "leader"
        }
    
    def test_post_create_new_user(self):
        res = requests.post(self.url, data=self.vaild_data)
        res_dict = json.loads(res.text)
        res_string_indent = json.dumps(res_dict, indent=2)
        print(res_string_indent)


if __name__ == "__main__":
    create_user = CreatUser("https://reqres.in/api/users")
    create_user.test_post_create_new_user()
