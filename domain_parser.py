#!/usr/bin/python3
import requests
import re

#parses from malwaredomains.com

urls = ['http://cybercrime-tracker.net/all.php', 'http://mirror1.malwaredomains.com/files/domains.txt', 'http://malc0de.com/bl/ZONES']
output = ['cybercrimetracker.txt', 'malwaredomains.txt', 'malcode.txt']


for index, url in enumerate(urls, start=0):
    print('Getting {t}'.format(t=url))
    resp = requests.get(url)
    txt = resp.text
    lines = txt.splitlines()
    domains = []
    for line in lines:
        match = re.search(r'\b((xn--)?[a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,}\b', line)
        if match:
            domains.append(match.group())

    fn = output[index]
    f = open(fn, 'w')
    print('Writing {l} \n'.format(l=fn))
    for line in domains:
        if 'malc0de.com' not in line and 'www.malwaredomains.com' not in line:
            print(line, file=f)
    f.close()

