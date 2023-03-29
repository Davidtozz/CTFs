import re
import requests

response = requests.post("http://gabibbo-says.challs.olicyber.it", data={"gabibbo": "angry"})
flag = re.findall("flag{.*}", response.text)[0]

print(flag)