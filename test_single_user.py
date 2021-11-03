import requests
import json


class SingleUser:
    def __init__(self, url) -> None:
        self.url = url

    def test_get_single_user(self):
        res = requests.get(self.url)
        res_dict = json.loads(res.text)
        res_string_indent = json.dumps(res_dict, indent=2)
        print(res_string_indent)


if __name__ == "__main__":
    single_user = SingleUser("https://reqres.in/api/users/2")
    single_user.test_get_single_user()
    single_user_invalid = SingleUser("https://reqres.in/api/user/23")
    single_user_invalid.test_get_single_user()
