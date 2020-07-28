import requests
from pprint import pprint

res = requests.get('https://baidu.com')

print(res.status_code)

