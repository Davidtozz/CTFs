#!/bin/python3

import re
import os
import requests
import logging
#logging.disable()


# Per le challenge web
#URL = os.environ.get("URL", )

flag_regex = "flag{.*}"

r = requests.post("http://gabibbo-says.challs.olicyber.it", data={
    "gabibbo": "angry"
})

print(r.headers)


flag = re.findall(flag_regex, r.text)[0]

print(flag)