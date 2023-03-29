from zipfile import ZipFile

with open("italian.txt", "rb") as wordlist:
    for word in wordlist:
        try:
            ZipFile("flag.zip").extractall(pwd=word.strip())
        except:
            continue
        else:
            print("Password found:", word.decode().strip())
            exit(0)