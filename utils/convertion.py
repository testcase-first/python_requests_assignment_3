import json

def string_prettify(response):
    """convert string to dictionary and then dictionary to prettified string
    Takes response.text
    """
    res_dict = json.loads(response)
    res_string = json.dumps(res_dict, indent=2)
    return res_string
