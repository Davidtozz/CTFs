import requests

print(requests.post("http://web-08.challs.olicyber.it/login", data={"username":"admin", "password":"admin"}).text)