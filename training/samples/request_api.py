import requests
import json
import urllib.request
from PIL import Image
r = requests.get('https://dog.ceo/api/breeds/image/random')
if r.status_code == 200:
    try:
        pretty_json =json.dumps(r.json(),indent=2)
    except:
        print("not a json")
        exit()
    print(f'Pretty: {pretty_json}')
else:
    print(f"error {r.status_code}")
msg= r.json()
urllib.request.urlretrieve(
  msg['message'],
   "gfg.png")
  
img = Image.open("gfg.png")
img.show()
