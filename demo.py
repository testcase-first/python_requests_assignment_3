import requests

info_dt = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}

# response = requests.post("https://reqres.in/api/register", data=info_dt)
# print(response.reason)
# print(response.status_code)
# print(response.text)

response = requests.get('https://reqres.in/api/register', data=info_dt)
print(response.status_code)
print(response.text)
