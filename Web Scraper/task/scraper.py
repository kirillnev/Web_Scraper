import requests

MSG = {
    'error_status_code': 'Invalid quote resource!'
}

CONTENT_KEY = 'content'

url = input()
# url = 'http://api.quotable.io/quotes/-4WQ_JwFWI'
response = requests.get(url)
if response.status_code == 200:
    json_data = response.json()
    if CONTENT_KEY in json_data:
        print(json_data['content'])
    else:
        print(MSG['error_status_code'])
else:
    print(MSG['error_status_code'])
