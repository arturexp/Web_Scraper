import requests
import json
from bs4 import BeautifulSoup

url = input("Input the URL:\n")
r = requests.get(url, headers={"accept-language": "en-US,en;q=0.9,uk;q=0.8,ru;q=0.7"})
db = {}
if r.status_code != 200 or 'imdb' not in url:
    print("\nInvalid movie page!")
else:
    content = BeautifulSoup(r.content, 'html.parser')
    t = content.find('title').text
    d = content.find('script', {'type': "application/ld+json"})
    d = str(d).replace('<script type="application/ld+json">', '').replace('</script>', '')
    d = json.loads(d)
    if d['@type'] == 'Movie' or d['@type'] == "TVSeries":
        db['title'] = d['name']
        disc = str(content.find('div', {'class': 'summary_text'}).text)
        disc = disc.strip()
        db['description'] = disc
    else:
        print("\nInvalid movie page!")
    print(db)

