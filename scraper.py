import requests
import json
from bs4 import BeautifulSoup

url = input("Input the URL:\n")
r = requests.get(url)
if r.status_code == 200:
    with open('source.html', 'wb') as file:
        file.write(r.content)
    print('\nContent saved.')
else:
    print('The URL returned', str(r.status_code) + '!')
