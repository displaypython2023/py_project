import requests
import cProfile
import json
import pprint
from urllib.request import urlopen
r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
r.status_code
r.headers['content-type']
r.encoding
r.text
pretty_json =json.dumps(r.json(),indent=2)
print(f'Pretty: {pretty_json}')

