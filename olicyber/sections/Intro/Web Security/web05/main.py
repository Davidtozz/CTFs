import requests as req

print(req.get(url="http://web-05.challs.olicyber.it/flag", cookies={"password" : "admin"}).text)