#!/usr/bin/python3
import requests
import re

# urls list containts the urls of the threat intel site that list the malicous domains
# output list is the files that should be written to for each threat intel site
urls = ['http://cybercrime-tracker.net/all.php', 'http://mirror1.malwaredomains.com/files/domains.txt', 'http://malc0de.com/bl/ZONES', 'https://urlhaus.abuse.ch/downloads/text/', 'http://osint.bambenekconsulting.com/feeds/c2-dommasterlist-high.txt']
output = ['cybercrimetracker.txt', 'malwaredomains.txt', 'malcode.txt', 'urlhaus.txt', 'c2-dommasterlist-high.txt']

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
        if 'malc0de.com' not in line and 'www.malwaredomains.com' and 'bambenekconsulting.com' not in line:
            print(line, file=f)
    f.close()

