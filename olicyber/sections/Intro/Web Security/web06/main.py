import requests

cookie = requests.get("http://web-06.challs.olicyber.it/token").cookies

print(requests.get("http://web-06.challs.olicyber.it/flag", cookies=cookie).text)