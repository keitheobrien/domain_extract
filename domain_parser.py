#!/usr/bin/python3
import requests
import re

#parses from malwaredomains.com

resp = requests.get("http://malc0de.com/bl/ZONES")
txt = resp.text

lines = txt.splitlines()

domains = []
for line in lines:
    match = re.search(r'\b((xn--)?[a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,}\b', line)
    if match:
        domains.append(match.group())

fn = "malcode.txt"
f = open(fn, 'w')
for line in domains:
    if 'malc0de.com' not in line and 'www.malwaredomains.com' not in line:
        print(line, file=f)
f.close()

