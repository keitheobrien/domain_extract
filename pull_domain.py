import requests
import re

#parses from malwaredomains.com

resp = requests.get("http://mirror1.malwaredomains.com/files/domains.txt")
txt = resp.text

lines = txt.splitlines()

domains = []
for line in lines:
    match = re.search(r'\b((xn--)?[a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,}\b', line)
    if match:
        domains.append(match.group())

fn = "malwaredomains.txt"
f = open(fn, 'w')
for line in domains:
    print(line, file=f)
f.close()