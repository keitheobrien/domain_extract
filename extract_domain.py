import tldextract
from bs4 import BeautifulSoup
import requests

resp = requests.get("http://cybercrime-tracker.net/all.php")
txt = resp.text

soup = BeautifulSoup(txt, 'html.parser')
#Pull out the text from the response
prelines = soup.text.strip()
#Add text to list
lines = prelines.split()

domains = []
for line in lines:
    domain = tldextract.extract(line)
    domains.append(domain.subdomain + domain.registered_domain)

print(domains)

domains_formated = list(filter(None, domains))

fn = "cybercrimetracker.txt"
f = open(fn, 'w')
for line in domains_formated:
    print(line, file=f)
f.close()
