# binario, esadecimale, base64

import requests, base64, binascii, re


example = '''
Veloce! Ho bisogno del tuo aiuto! Abbiamo due minuti al massimo...
Ti darÃ² dei dati in formato JSON... Perfavore ricodificali e rimandameli indietro in formato JSON!
Il JSON di risposta deve avere un campo 'answer' che contiene la tua risposta

Converti questo a binario (Senza lo 0b iniziale)!
{"message": "CJVwjlIgzcsnrwWJWoxvKRcYEaeiTRh"}
Ora dammi una risposta!

'''


mystring = r"Chihuahua124332grb2".encode('utf-8')
print(mystring.hex())

url = "http://based.challs.olicyber.it:10600/"

response = ""

while(True):
    
    response = requests.get(url).text

    message = re.findall("(.*?)", response)[1]
    
    if response.find("da"):
        if response.find("binario"):
            response = requests.post(url=url, data={"answer": f"{''.join(format(ord(i), '08b') for i in message)}"})
            pass
        elif response.find("esadecimale"): # TODO
            pass
        else: # base64
            pass
    else: #? a ->
        if response.find("binario"): # TODO
            pass
        elif response.find("esadecimale"): # TODO
            pass
        else: # base64
            pass
    