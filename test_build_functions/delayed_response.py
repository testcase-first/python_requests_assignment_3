from utils.api_endpoints import delayed_response_endpoint
from utils.response import response
from utils.convertion import string_prettify


def test_delayed_response():
    res = response('GET', delayed_response_endpoint)
    res_prettified_string = string_prettify(res.text)
    return res_prettified_string, res.status_code, res.elapsed.seconds


# import problem showed
if __name__ == "__main__":
    test_delayed_response()
