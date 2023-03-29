import requests, re

infinite_url = 'http://infinite.challs.olicyber.it'

session  = requests.Session() # Persistent session cookie
cookie= {"secret":"sqsifwbIxbGrC4OBVw2QLrJG9AOCOQsymTq1fEsrCQ7ivb10XdEewRhST+7DVG5g"}

# Math test 
def math_test(body: str):

    # First, we need to get the math test string
    prompt: str = re.compile(r'<p>(.+?)</p>').findall(body)[0]
    
    # We proceed to remove alphabetic characters
    prompt: str = re.sub(r"[a-zA-Z]","",prompt).replace(" ", "")[:-1]

    # Finally, we need to get the answer and submit it
    a,b  = prompt.split("+")
    result: int = int(a)+int(b)
    return session.post(infinite_url, f'sum={result}', cookies=cookie).text

# Grammar test
def grammar_test(body: str):
    
    prompt = re.compile(r'<p>[^"].*[^"]</p>').findall(body)
    
    result = re.findall(r'("[^"]*")|[^"\s]+', str(prompt)) # Get the filtered prompt, causing ''s to appear in the result
    
    guess, target = list(filter(None, result)) # filter removes empty strings
    
    guess: str = "".join(guess)
    target: str = "".join(target)
    
    occurences: int = target.count(guess)
    
    print(f"Guess: {guess} Target: {target}") # DEBUG
    return session.post(infinite_url, f"letter={occurences}&submit=Submit", cookies=cookie).text 

def art_test(body: str):
    
    # Look fot the color to find
    color_regex = r'<p>(.+?)</p>'
    prompt: str = re.findall(color_regex, body)[0]
    
    # Match the color, then submit it
    if "Rosso" in prompt:
        return session.post(infinite_url, f"Rosso=", cookies=cookie).text
    if "Verde" in prompt:
        return session.post(infinite_url, f"Verde=", cookies=cookie).text
    if "Blu" in prompt:
        return session.post(infinite_url, f"Blu=", cookies=cookie).text

for i in range(10000):
    
    response = session.get(infinite_url, cookies=cookie)
    body = response.text
    
    if "flag" in body:
        with open("flag.txt", "w") as f:
            f.write(body)
            f.close()
        
    page_type: str = re.compile(r'<h2>(.*)</h2>').findall(body)[0]
    
    print(f"({i}) Page type: {page_type}\n") # DEBUG
    
    if i > 500:
        with open(f">500/{i}.html", "w+") as f:
            f.write(body)
            f.close()
       
    if page_type == "MATH TEST":
        math_test(body=body)
        
    elif page_type == "GRAMMAR TEST": 
        body = grammar_test(body=body)
    
    else:
        body = art_test(body=body)