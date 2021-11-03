import requests
from requests.api import get

def response(method="", endpoint="", **kwargs):
    """returns response for given method, endpoint and kwargs"""
    res = requests.request(method=method, url=endpoint, **kwargs)
    return res

# this is just a test and way to know how it works
# if __name__ == "__main__":
#     r = response('get', "https://example.com")
#     print(r)
#     print(type(r))
