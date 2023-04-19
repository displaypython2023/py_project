import requests
import json
import time
import urllib.request
from PIL import Image
import datetime
def todayAt (hr, minutes=0, sec=0, micros=0):
    now_time = datetime.datetime.now()
    return now_time.replace(hour=hr, minute=minutes, second=sec, microsecond=micros)    
while datetime.datetime.now() < todayAt (16,10):
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
    """img = Image.open("gfg.png")
    img.show()
    img.close()"""
    with Image.open('gfg.png') as test_image:
        test_image.show()
        time.sleep(3)
