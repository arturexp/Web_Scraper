import requests
import json
from bs4 import BeautifulSoup
import string

art = []
link = []
r = requests.get('https://www.nature.com/nature/articles')
if r.status_code == 200:
    data = BeautifulSoup(r.content, 'html.parser')
    tag_news = data.find_all('article')   # data.find_all('span', {'data-test': 'article.type'})

    for i in tag_news:
        if i.find('span', {'data-test': 'article.type'}).text == "News":
            link = "https://www.nature.com" + i.find('a', {"data-track-action": "view article"}).get("href")
            new_article = requests.get(link)
            article = BeautifulSoup(new_article.content, 'html.parser')
            article_title = article.find('h1', {'class': 'article-item__title'}).text
            outtab = "_" * 32
            intab= string.punctuation
            trantab = str.maketrans(intab, outtab)

            article_title = article_title.translate(trantab)

            article_title = article_title.replace('_', '')
            article_title = article_title.replace(' ', '_')

            article_body = article.find('div', {'class': 'article__body'}).text
            article_body = article_body.strip()
            with open(article_title + '.txt', 'wb') as file:
                file.write(str.encode(article_body))

else:
    print('The URL returned', str(r.status_code) + '!')
