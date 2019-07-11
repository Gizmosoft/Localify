import requests
import json

class Geolocation():
    send_url = 'http://api.ipstack.com/check?access_key=7bb628ded9e1540f63ab77df527c2e78'
    r = requests.get(send_url)
    j = json.loads(r.text)
    user_city = j['city']
    user_zip = j['zip']
    # loc = j['location']       #get location object
    # print(loc)

    print(user_city)
    print(user_zip)
