import requests 

header = {"Accept":"application/xml"}

print(requests.get("http://web-04.challs.olicyber.it/users", headers=header).text)