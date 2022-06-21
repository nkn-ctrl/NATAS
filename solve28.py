#!bin/python3
import requests

session = requests.Session()

url = "http://natas28.natas.labs.overthewire.org/"
auth_username = "natas28"
auth_password = "JWwR438wkgTsNKBbcJoowyysdM82YjeF"

specialChars = ['\'','"','#','-','*','=','(',')',' ']
for char in specialChars:
    r = session.get(url,auth=(auth_username,auth_password),data={'query':f'{char}'})

print(r.text)
print(r.url)