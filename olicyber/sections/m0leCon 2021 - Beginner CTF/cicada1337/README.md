# Writeup: [cicada1337](https://training.olicyber.it/challenges#challenge-160) di @df1665 ([pwnth3m0le](https://pwnthem0le.polito.it/)) 
 


- La challenge è suddivisa in vari livelli da superare, ognuno dei quali richiede un'abilità specifica per essere risolta. Ogni livello è stato pensato per essere di difficoltà crescente, in modo da mettere alla prova le diverse abilità dei partecipanti. Come si può notare dal nome, questa challenge si ispira alla famosa serie di puzzle da parte di [Cicada 3301](https://it.wikipedia.org/wiki/Cicada_3301).
  
  Tenete bene a mente quest'ultima informazione, ci servirà dopo!
- ## Livello 1
  
  La challenge inizia con un'immagine, **`level1.png`**:
  
  ![](https://raw.githubusercontent.com/Davidtozz/CTFs/main/olicyber/sections/m0leCon%202021%20-%20Beginner%20CTF/cicada1337/level1.png)
- Un'URL è nascosto all'interno dell'immagine. Per trovarlo, possiamo usare **`strings`** e abbinarlo a `grep` come di seguito:
  ```bash
  strings level1.png | grep http
  ```
  Output: https://postimg.cc/WdNhTrMR
- ## Livello 2
  
  Seguendo il link trovato, verremo indirizzati a un'altra immagine, **`pidgey.png`**
  
  ![](https://raw.githubusercontent.com/Davidtozz/CTFs/main/olicyber/sections/m0leCon%202021%20-%20Beginner%20CTF/cicada1337/pidgey.jpg)
- Per superare il livello 2 vi sono varie strade che possiamo percorrere. Ad esempio, se analizziamo l'immagine con **`exiftool`**:
  ```bash
  exiftool pidgey.png
  ```
  
  Notiamo un dettaglio interessante:
  ```
  Comment                              : postimg.cc/7bz4c6Jg
  ```
- # Livello 3
  
  Nell'immagine `pidgey.png` abbiamo trovato un link, che ci porta alla terza (ed ultima) immagine:
  `congratulations.png`
  
  ![](https://raw.githubusercontent.com/Davidtozz/CTFs/main/olicyber/sections/m0leCon%202021%20-%20Beginner%20CTF/cicada1337/congratulations.jpg)
- Ancora una volta dovremo analizzare un'immagine alla ricerca di informazioni nascoste, in questo caso **tre numeri primi**. Come per la precedente immagine, iniziamo la nostra ricerca con `exiftool`:
  ```bash 
  exiftool congratulations.png
  ```
  
  
  Nell'output, notiamo 3 numeri che corrispondono a ciò che stiamo cercando:
  
  ```
  Comment                                         : 1033    
  Image Size                                      : 641x587
  ```
  
  Moltiplicandoli tra loro, otteniamo `388683811`. 
  Dunque il link al subreddit sarà: https://www.reddit.com/r/388683811/
- # Livello 4
- Questa è la nostra ultima tappa, oltre la quale si cela la flag che cerchiamo. Nel subreddit vi sono due post:
	- Il [primo](https://www.reddit.com/r/388683811/comments/tcdcpw/_/), che contiene un testo
	- Il [secondo](https://www.reddit.com/r/388683811/comments/tcddrw/_/), che contiene una serie di coppie di numeri nel formato X:Y
- Questi post inizialmente non sembrano rivelare informazioni utili a procedere. Di conseguenza, torno indietro e controllo se mi sono perso qualcosa.
  
  Noto che la descrizione della challenge:
  *"Don't worry, you won't have to scan QRs across the globe."*
  
  È un chiaro riferimento al primo puzzle di [Cicada 3301](https://it.wikipedia.org/wiki/Cicada_3301)! Dunque, procedo cercando una [writeup in merito](https://anilcelik.medium.com/en-tryhackme-cicada-3301-vol-1-write-up-9f7eb4fec1fd) sperando in indizi utili a procedere.
- Scorrendo tra i vari step, noto che uno di questi è molto simile al [secondo](https://www.reddit.com/r/388683811/comments/tcddrw/_/) post nel subreddit:
  
  ![](https://miro.medium.com/v2/resize:fit:720/0*pJSsxvaxLpxgxskT)
  
  L'autore dell'articolo scrive qualcosa che cattura subito la mia attenzione:
  ***What I understand from here is, for first one, I should go to 1st line and take the 6th character and so on.(...)***
  
  Tutto torna: il [secondo](https://www.reddit.com/r/388683811/comments/tcddrw/_/) post del subreddit dà le coordinate dei caratteri che comporranno la nostra flag all'interno del [primo](https://www.reddit.com/r/388683811/comments/tcdcpw/_/) post!
  
  Non ci resta che ricreare la nostra flag:
  ```python
  # main.py
  with open("prompt.txt", "r") as f:
      prompt = f.readlines()
  
  coords = [ 
      (9, 43), (19, 50), (5, 35), (1, 1), (14, 41), 
      (19, 10), (12, 11), (7, 44), (5, 23), (20, 11),
      (6, 58), (16, 22), (20, 63), (8, 12), (17, 27),
      (2, 34), (9, 4), (20, 34), (19, 57), (15, 35),
      (8, 44), (15, 80), (18, 29), (1, 8)
  ]
  
  flag = ""
  for x, y in coords:
      flag += prompt[x-1][y-1]
  
  print(flag)
  ```
  Per semplicità, ho incluso il testo del [primo](https://www.reddit.com/r/388683811/comments/tcdcpw/_/) post all'interno del file `prompt.txt`. 
  
  L'output sarà la nostra flag: `PTM{SEEKANDYOUSHALLFIND}`
