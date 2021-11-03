import requests
import json


class DelayedResponse:
    def __init__(self, url) -> None:
        self.url = url
    
    def test_delayed_response(self):
        res = requests.get(self.url)
        res_dict = json.loads(res.text)
        res_string_indent = json.dumps(res_dict, indent=2)
        print(res_string_indent)


if __name__ == "__main__":
    delayed_response = DelayedResponse("https://reqres.in/api/users?delay=3")
    delayed_response.test_delayed_response()
