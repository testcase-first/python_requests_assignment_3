import requests
import json


class UserList:
    def __init__(self, url):
        self.url = url
    
    def test_get_list_users(self):
        res = requests.get(self.url)
        res_dict = json.loads(res.text)
        res_string_indent = json.dumps(res_dict, indent=2)
        print(res_string_indent)
        print(type(res_string_indent))


if __name__ == "__main__":
    user_list = UserList("https://reqres.in/api/users?page=2")
    user_list.test_get_list_users()